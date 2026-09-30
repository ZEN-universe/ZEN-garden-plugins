"""Variables supplied by ``plugin_template_add_new_constraint``.

Add new variable classes to this package and re-export them here before
registering them in ``plugin.py``.
"""

from .new_variable import NewVariable

__all__ = ["NewVariable"]
