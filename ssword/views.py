# -*- coding: utf-8 -*-
"""
    ssword.views
    ~~~~~~~~~~~~

    This module contains the views for the
    ssword Plugin.

    :copyright: (c) 2018 by zhongkui li.
    :license: BSD License, see LICENSE for more details.
"""
from flask import Blueprint, flash
from flask_babelplus import gettext as _

from flaskbb.utils.helpers import render_template
from flaskbb.plugins.models import PluginRegistry


ssword_bp = Blueprint("ssword_bp", __name__, template_folder="templates")


@ssword_bp.route("/")
def index():
    plugin = PluginRegistry.query.filter_by(name="ssword").first()
    if plugin and not plugin.is_installed:
        flash(_("Plugin is not installed."), "warning")

    return render_template("index.html", plugin=plugin)
