"""Define the equality linking the template parameter and variable."""

from zen_garden.model.component_types.constraint import GenericConstraint

from zen_garden_plugins.plugin_template_add_new_constraint.masks import (
    NewConstraintMask,
)


class NewConstraint(GenericConstraint):
    """Set ``new_variable`` equal to ``new_parameter`` at every valid node."""

    masks = {"new_constraint": [NewConstraintMask]}

    @classmethod
    def build(cls, model_constructor) -> None:
        """Construct and register the node-wise equality constraint.

        Linopy aligns the variable and parameter by their shared node
        coordinate. :meth:`GenericConstraint.add_constraint` then resolves the
        masks declared for ``new_constraint``, aligns them to the resulting
        Linopy constraint, and passes the combined mask to the optimization
        model. The dictionary key in :attr:`masks` must therefore exactly match
        the name passed to ``add_constraint``.

        Args:
            model_constructor: Active ZEN-garden model constructor containing
                the registered optimization variables and parameters.
        """
        optimization_model = model_constructor.optimization_model
        constraints = (
            optimization_model.variables["new_variable"]
            == optimization_model.parameters.new_parameter
        )
        cls.add_constraint(model_constructor, "new_constraint", constraints)
