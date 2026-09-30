import os

import pytest
from zen_garden import EventPublisher


@pytest.fixture(autouse=True)
def isolate_plugin_observers():
    """Prevent plugin event handlers from leaking between end-to-end tests."""
    EventPublisher.deregister_all()
    yield
    EventPublisher.deregister_all()


@pytest.fixture
def fixtures_path():
    """Return the path containing the standard end-to-end fixtures."""
    return os.path.join(os.path.dirname(__file__), "fixtures")
