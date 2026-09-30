.. _implementation.implementing_plugins:

####################################
Step 1: Getting started
####################################
This guide walks you through creating a plugin for ZEN-garden from scratch. There
are two ways to develop a plugin:

1. With this repository (recommended for beginners): Fork this repository and develop your plugin here
2. In a separate repository: Create your own plugin repository and install it as a Python package

If you implement your plugin in this repository, you can **fork this repository**.
The template plugin in this repository is a working example. Use it as a reference when building
your own plugin.

- ``zen_garden_plugins/plugin_template/plugin.py`` — Simple example code
- ``docs/files/available_plugins/template_plugin/`` — Example documentation
- ``tests/plugin_template/test_plugin.py`` — Example test implementation

**Copy ``plugin_template/``** and rename it (e.g., ``my_awesome_plugin/``).

The following three locations are important for your plugin:

- ``zen_garden_plugins/my_awesome_plugin/plugin.py`` — Your plugin code
- ``docs/files/available_plugins/my_awesome_plugin/`` — Your plugin documentation
- ``tests/my_awesome_plugin/test_my_awesome_plugin.py`` — Your plugin tests
- ``pyproject.toml`` — Place to register your plugin so that ZEN-garden sees it



####################################
Step 2: Update ``pyproject.toml``
####################################

Tell Python that your plugin is a ZEN-garden plugin by adding an entry point
in ``pyproject.toml``:

.. code-block:: toml

    [project.entry-points."zen_garden.plugins"]
    plugin_template = "zen_garden_plugins.plugin_template.plugin"
    my_awesome_plugin = "zen_garden_plugins.my_awesome_plugin.plugin"

The entry point name (``my_awesome_plugin``) is what users write in the ZEN garden
``config.yaml``.

#################################################
Step 3: Prepare the documentation of your plugin
#################################################

Create ``docs/files/available_plugins/my_awesome_plugin/`` with:

- ``my_awesome_plugin.rst`` — Add high-level description of your plugin
- Any other documentation users need.

See ``template_plugin.rst`` for an example.

#############################################
Step 4: Prepare testing for your plugin
#############################################

Create a ``tests/my_awesome_plugin`` directory including a test file
(e.g., ``test_my_awesome_plugin.py``).

This is where you write unit tests for your plugin.

########################################################################
Step 5: Write your plugin code, testing, and documentation
########################################################################

Every ``plugin.py`` must have:

1. A `Config` class with default settings:

   .. code-block:: python

       from zen_garden import ConfigBase

       class Config(ConfigBase):
           """Configuration for my plugin."""
           my_setting: str = "default_value"

2. One or more functions decorated with ``@EventPublisher.register``:

   .. code-block:: python

       from zen_garden import Event, EventPublisher

       @EventPublisher.register(Event.after_model_schema_creation)
       def my_plugin_logic(model_schema):
           """This runs at a specific point in ZEN-garden's workflow."""
           # Your code goes here!
           pass

**How it works:**

- ZEN-garden has a workflow with specific points where plugins can "hook in"
- Each hook is an "event" (e.g., ``after_model_schema_creation``)
- Your function is called automatically when ZEN-garden reaches that event
- ZEN-garden passes relevant objects to your function

**Available events:**

See ``zen_garden.plugin_system.events.Event`` for all available events.

Each event passes specific keyword arguments. Check the ZEN-garden source or docstrings
to see what each event provides.

**Access your configuration**

Inside your plugin function, access the settings passed from ZEN-garden:

.. code-block:: python

    @EventPublisher.register(Event.after_model_schema_creation)
    def my_plugin_logic(model_schema):
        # Get your plugin's config from ZEN-garden
        config = model_schema.config.plugins["my_plugin"]
        my_value = config["my_setting"]
        print(f"Using setting: {my_value}")


#####################################################
Step 6: Load and configure plugin in ZEN-garden
#####################################################

Install the plugin package into the same Python environment as ZEN-garden:

.. code-block:: shell

     uv pip install -e path/to/plugin_repository --no-deps

The ``-e`` flag installs it in *editable* mode, which means changes to your files
take effect immediately without reinstalling.

.. warning::
    If you change the pyproject.toml or add new dependencies, you must reinstall
    the plugin.

Activate your plugin in the ``config.yaml`` file of ZEN-garden:

.. code-block:: yaml

    plugins:
      my_awesome_plugin:
        my_setting: "custom_value"

That's it! ZEN-garden will:

1. Find your installed plugin
2. Load your ``Config`` with the custom value
3. Call your decorated functions at the right event

