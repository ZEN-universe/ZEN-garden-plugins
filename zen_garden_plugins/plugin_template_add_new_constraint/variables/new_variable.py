"""Define the node-indexed optimization variable used by the template."""

from zen_garden.model.component_types.variable import GenericVariable


class NewVariable(GenericVariable):
    """Continuous variable constrained to equal ``new_parameter`` per node.

    ``GenericVariable`` constructs a continuous, unbounded variable by default.
    Override ``get_bounds`` or set the inherited ``integer``/``binary`` flags
    when adapting the template to a different mathematical formulation. Its
    indices and unit category match :class:`NewParameter`, allowing direct
    elementwise comparison in the constraint.
    """

    name = "new_variable"
    indices = ["set_nodes"]
    doc = "Dimensionless decision variable defined independently for every node"
    unit_category = {}
