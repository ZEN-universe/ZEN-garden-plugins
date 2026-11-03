.. _available_plugins.plugin_template_add_new_constraint:

Template: add a parameter, variable, and constraint
---------------------------------------------------

The ``plugin_template_add_new_constraint`` plugin is an extended template for
creating a ZEN-garden plugin that contributes optimization-model components. It
demonstrates how to:

* define a node-indexed input parameter with a default value and unit;
* define a node-indexed continuous variable;
* define a reusable structural mask;
* constrain the variable to equal the parameter at every valid node;
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

Mask definition
^^^^^^^^^^^^^^^

Structural masks control which indexed rows or columns are constructed. They
are built after parameters and before variables and constraints, so they may
depend on parameters, sets, configuration, time mappings, and other masks, but
not on variables or constraints. The example mask keeps nodes with a
non-missing ``new_parameter`` value. Because this parameter defaults to zero,
all configured nodes are active unless the input contains a missing value.

When one mask builds on another, list the required mask classes in its
``dependencies`` attribute and retrieve their constructed values from the
``registry`` argument. ZEN-garden constructs dependencies first and rejects
cyclic dependency graphs. A mask with no dependencies, like this example,
leaves ``registry`` unused.

.. literalinclude:: ../../../../zen_garden_plugins/plugin_template_add_new_constraint/masks/new_constraint_mask.py
   :language: python

Constraint definition
^^^^^^^^^^^^^^^^^^^^^

Constraint classes declare masks in a dictionary keyed by the exact name used
to register each constraint. Always call ``cls.add_constraint(...)`` for a
masked constraint: the helper retrieves the declared masks, combines multiple
masks with logical AND, aligns canonical dimensions to the Linopy constraint,
and forwards the resolved mask to the optimization model. Calling
``optimization_model.add_constraint(...)`` directly bypasses this mechanism.

Use a named composite mask when OR logic is required. Conditions that select
between different mathematical equations belong in the constraint's ``build``
method instead of a structural mask.

.. literalinclude:: ../../../../zen_garden_plugins/plugin_template_add_new_constraint/constraints/new_constraint.py
   :language: python

Module documentation
^^^^^^^^^^^^^^^^^^^^

.. automodule:: zen_garden_plugins.plugin_template_add_new_constraint.plugin
   :members:
   :undoc-members:
