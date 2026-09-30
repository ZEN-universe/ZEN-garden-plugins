"""Parameters supplied by ``plugin_template_add_new_constraint``.

Re-exporting component classes here keeps imports in ``plugin.py`` concise and
provides one obvious place to expose additional parameters.
"""

from .new_parameter import NewParameter

__all__ = ["NewParameter"]
