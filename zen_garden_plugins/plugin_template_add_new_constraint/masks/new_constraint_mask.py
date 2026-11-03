"""Define the structural mask used by the template constraint."""

from zen_garden.model.component_types.mask import GenericMask


class NewConstraintMask(GenericMask):
    """Select nodes for which ``new_parameter`` contains a valid value.

    Structural masks are built after parameters and before variables and
    constraints. Consequently, a mask may use parameters, sets, configuration,
    time mappings, or another declared mask, but it must not depend on a
    variable or constraint. List other mask classes in :attr:`dependencies`
    before retrieving their results from ``registry`` inside :meth:`build`.
    """

    name = "new_constraint_mask"
    # Add required mask classes here, for example:
    # dependencies = [SomeDependencyMask, AnotherDependencyMask]
    dependencies = []

    @classmethod
    def build(cls, model_constructor, registry):
        """Return a node-indexed boolean mask for the example components.

        Args:
            model_constructor: Active ZEN-garden model constructor containing
                the already constructed parameters.
            registry: Mask registry containing any masks listed in
                :attr:`dependencies`.

        Returns:
            A boolean ``xarray.DataArray`` that is true where ``new_parameter``
            is not missing.
        """
        # This mask has no dependencies, so ``registry`` is intentionally
        # unused. A dependent mask can access a accessed with
        # ``dependency_mask = registry[SomeDependencyMask]``.
        parameter = model_constructor.optimization_model.parameters.new_parameter
        return parameter.notnull()
