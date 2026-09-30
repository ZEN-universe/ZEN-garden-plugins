"""Register components provided by ``plugin_template_add_new_constraint``.

ZEN-garden discovers this module through the ``zen_garden.plugins`` entry point
in ``pyproject.toml``. Importing the module registers the event handler below.
The handler extends the model schema before input data is read and the
optimization model is constructed.
"""

from pydantic import Field
from zen_garden import ConfigBase, Event, EventPublisher, ModelSchema
from zen_garden.elements.energy_system import EnergySystem

from zen_garden_plugins.plugin_template_add_new_constraint.constraints import (
    NewConstraint,
)
from zen_garden_plugins.plugin_template_add_new_constraint.parameters import (
    NewParameter,
)
from zen_garden_plugins.plugin_template_add_new_constraint.variables import NewVariable


class Config(ConfigBase):
    """Validate settings under ``plugins.plugin_template_add_new_constraint``.

    The configuration demonstrates how a typed plugin setting is declared and
    documented. Users may write the following in their configuration file::

        plugins:
          plugin_template_add_new_constraint:
            include_constraint: true

    Add further typed Pydantic fields here when adapting the template. After
    validation, their values are available in
    ``model_schema.config.plugins["plugin_template_add_new_constraint"]``.
    """

    include_constraint: bool = Field(
        default=True,
        description="Whether to add new_constraint to the optimization model.",
    )


@EventPublisher.register(Event.after_model_schema_creation)
def add_new_constraint_components(model_schema: ModelSchema) -> None:
    """Attach the parameter, variable, and constraint to the energy system.

    Components are attached to ``EnergySystem`` because they are indexed only
    by nodes and do not belong to a carrier or technology. A parameter is added
    to both ``own_parameters`` (which declares where its input is stored) and
    ``parameters`` (the complete list processed by model construction).

    Args:
        model_schema: Mutable model blueprint supplied by ZEN-garden after its
            standard components have been registered.
    """
    config = model_schema.config.plugins["plugin_template_add_new_constraint"]
    if config["include_constraint"]:
        energy_system = model_schema.element_type_classes["EnergySystem"]
        if not issubclass(energy_system, EnergySystem):
            raise TypeError(
                "Expected the 'EnergySystem' schema entry to contain an "
                "EnergySystem subclass"
            )
        energy_system.own_parameters.append(NewParameter)
        energy_system.parameters.append(NewParameter)
        energy_system.variables.append(NewVariable)
        energy_system.constraints.append(NewConstraint)
