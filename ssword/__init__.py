# -*- coding: utf-8 -*-
"""
    ssword
    ~~~~~~

    A ssword Plugin for FlaskBB.

    :copyright: (c) 2018 by zhongkui li.
    :license: BSD License, see LICENSE for more details.
"""
import os
#import gevent
import threading
from werkzeug.contrib.cache import SimpleCache
from flaskbb.forum.models import Forum
from flaskbb.utils.helpers import render_template
from flaskbb.utils.forms import SettingValueType

from .views import ssword_bp
from .service.watchdog import watching
from .filter.dfaFilter import SimpleDFAFilter
from .loader.txtFileLoader import SimpleTxtFileLoader

__version__ = "0.1.0"

# connect the hooks
def flaskbb_extensions(app):
    print "calling ssword:flaskbb_extensions to initialize"
    ctx = app.app_context()
    ctx.push()
    ssword_base = os.path.join(os.path.dirname(__file__), "data")
    loader = SimpleTxtFileLoader(ssword_base)
    app.sswords = loader.load()
    SimpleDFAFilter.build()
    #gevent.spawn(watching, libpath)
    t = threading.Thread(target=watching, args=ssword_base)
    t.setDaemon(True)
    t.start()
    pass

def flaskbb_load_migrations():
    return os.path.join(os.path.dirname(__file__), "migrations")

def flaskbb_load_translations():
    return os.path.join(os.path.dirname(__file__), "translations")

def flaskbb_load_blueprints(app):
    app.register_blueprint(ssword_bp, url_prefix="/ssword")

def flaskbb_tpl_before_navigation():
    return render_template("ssword_navlink.html")

def flaskbb_tpl_form_new_topic_before(form):
    #f = SimpleDFAFilter()
    print "calling flaskbb_tpl_form_new_topic_before"

def flaskbb_tpl_form_new_post_before(post):
    #f = SimpleDFAFilter()
    print "flaskbb_tpl_form_new_post_before"



# plugin settings
SETTINGS = {
    "path": {
        "value": "~/sswords/",
        "value_type": SettingValueType.string,
        "name": "library path",
        "description": "sensitive"
    }
}
