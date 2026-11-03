"""Structural masks supplied by ``plugin_template_add_new_constraint``.

Add new mask classes to this package and re-export them here before declaring
them on a variable or constraint class.
"""

from .new_constraint_mask import NewConstraintMask

__all__ = ["NewConstraintMask"]
