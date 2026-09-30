import importlib
import sys
import types
from types import SimpleNamespace

from zen_garden import ConfigBase


def _load_plugin_with_fake_events(monkeypatch):
    """
    Import plugin module with a fake zen_garden events module.

    Behaves like the Zen garden plugin loader and returns all modules, events and
    calls loaded.
    """
    calls = []

    class Event:
        after_model_schema_creation = object()

    class EventPublisher:
        @staticmethod
        def register(event):
            def decorator(func):
                calls.append((event, func))
                return func

            return decorator

    class ModelSchema:
        pass

    zen_garden = types.ModuleType("zen_garden")
    zen_garden.ConfigBase = ConfigBase
    zen_garden.Event = Event
    zen_garden.EventPublisher = EventPublisher
    zen_garden.ModelSchema = ModelSchema

    monkeypatch.setitem(sys.modules, "zen_garden", zen_garden)
    monkeypatch.delitem(
        sys.modules, "zen_garden_plugins.plugin_template.plugin", raising=False
    )

    module = importlib.import_module("zen_garden_plugins.plugin_template.plugin")
    return module, Event, calls


def test_plugin_exposes_config_schema_with_default(monkeypatch):
    """Test the plugin config schema and its default values."""
    module, _event, _calls = _load_plugin_with_fake_events(monkeypatch)

    assert issubclass(module.Config, ConfigBase)
    assert module.Config().example_setting == "default_value"
    assert module.Config().example_number == 100


def test_plugin_registers_handler_for_test_event1(monkeypatch):
    """Test handler registered for test event1."""
    module, event, calls = _load_plugin_with_fake_events(monkeypatch)

    assert len(calls) == 1
    registered_event, registered_function = calls[0]
    assert registered_event is event.after_model_schema_creation
    assert registered_function is module.extend_model


def test_plugin_handler_reads_config_from_model_schema(monkeypatch, capsys):
    """Test the handler reads the validated config from the model schema."""
    module, _event, _calls = _load_plugin_with_fake_events(monkeypatch)
    model_schema = SimpleNamespace(
        config=SimpleNamespace(
            plugins={
                "plugin_template": {
                    "example_setting": "configured_value",
                    "example_number": 42,
                }
            }
        )
    )

    module.extend_model(model_schema)

    output = capsys.readouterr().out
    assert "[Plugin Template] Example setting: configured_value" in output
    assert "[Plugin Template] Example number: 42" in output
    assert "[Plugin Template] Plugin loaded successfully!" in output
