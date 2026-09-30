"""Define the equality linking the template parameter and variable."""

from zen_garden.model.component_types.constraint import GenericConstraint


class NewConstraint(GenericConstraint):
    """Set ``new_variable`` equal to ``new_parameter`` at every node."""

    @classmethod
    def build(cls, model_constructor) -> None:
        """Construct and register the node-wise equality constraint.

        Linopy aligns the variable and parameter by their shared node
        coordinate, producing one equality for each configured node. Adapt the
        expression here to implement a different relation, and choose a unique
        name in ``add_constraint`` so the result can be identified reliably.

        Args:
            model_constructor: Active ZEN-garden model constructor containing
                the registered optimization variables and parameters.
        """
        optimization_model = model_constructor.optimization_model
        constraints = (
            optimization_model.variables["new_variable"]
            == optimization_model.parameters.new_parameter
        )
        optimization_model.add_constraint("new_constraint", constraints)
