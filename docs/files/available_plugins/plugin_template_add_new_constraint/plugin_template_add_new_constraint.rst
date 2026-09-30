.. _available_plugins.plugin_template_add_new_constraint:

Template: add a parameter, variable, and constraint
---------------------------------------------------

The ``plugin_template_add_new_constraint`` plugin is an extended template for
creating a ZEN-garden plugin that contributes optimization-model components. It
demonstrates how to:

* define a node-indexed input parameter with a default value and unit;
* define a node-indexed continuous variable;
* constrain the variable to equal the parameter at every node;
* expose a typed plugin configuration setting; and
* register all components through a ZEN-garden event handler.

Enable the plugin in a ZEN-garden configuration as follows:

.. code-block:: yaml

   plugins:
     plugin_template_add_new_constraint:
       include_constraint: true

Node-specific values for ``new_parameter`` can be supplied in
``energy_system/new_parameter.csv``:

.. code-block:: text

   node,new_parameter
   DE,2.5
   CH,7.5

Plugin registration
^^^^^^^^^^^^^^^^^^^

.. literalinclude:: ../../../../zen_garden_plugins/plugin_template_add_new_constraint/plugin.py
   :language: python

Parameter definition
^^^^^^^^^^^^^^^^^^^^

.. literalinclude:: ../../../../zen_garden_plugins/plugin_template_add_new_constraint/parameters/new_parameter.py
   :language: python

Variable definition
^^^^^^^^^^^^^^^^^^^

.. literalinclude:: ../../../../zen_garden_plugins/plugin_template_add_new_constraint/variables/new_variable.py
   :language: python

Constraint definition
^^^^^^^^^^^^^^^^^^^^^

.. literalinclude:: ../../../../zen_garden_plugins/plugin_template_add_new_constraint/constraints/new_constraint.py
   :language: python

Module documentation
^^^^^^^^^^^^^^^^^^^^

.. automodule:: zen_garden_plugins.plugin_template_add_new_constraint.plugin
   :members:
   :undoc-members:
