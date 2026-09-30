"""Define the node-indexed input parameter used by the template constraint."""

from zen_garden.model.component_types.parameter import GenericParameter


class NewParameter(GenericParameter):
    """Input value to which ``new_variable`` is constrained at each node.

    ``indices`` determines both the expected input dimensions and the parameter
    dimensions in the optimization model. Users may provide node-specific data
    in ``energy_system/new_parameter.csv`` with columns ``node`` and
    ``new_parameter``.

    If no explicit value is supplied, ZEN-garden uses zero. ``default_unit``
    names an existing energy-system attribute whose unit is reused; referencing
    ``discount_rate`` therefore makes this example parameter dimensionless.
    Adapt ``indices``, ``unit_category``, and the defaults together when using
    this class as a template for a physical quantity.
    """

    name = "new_parameter"
    indices = ("set_nodes",)
    doc = "Dimensionless input value specified independently for every node"
    unit_category = {}
    default_value = 0
    default_unit = "discount_rate"
