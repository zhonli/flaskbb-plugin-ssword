# -*- coding: utf-8 -*-
"""
    ssword
    ~~~~~~

    A ssword Plugin for FlaskBB.

    :copyright: (c) 2018 by zhongkui li.
    :license: BSD License, see LICENSE for more details.
"""
import os
from flask_babelplus import lazy_gettext as _

from flaskbb.forum.models import Forum
from flaskbb.forum.exceptions import StopNewPost, StopEditPost, StopNewTopic
from flaskbb.utils.helpers import render_template
from flaskbb.utils.forms import SettingValueType

from .views import ssword_bp
from .service.watchsvc import watching_async
from .filter.dfaFilter import SimpleDFAFilter
from .loader.txtFileLoader import SimpleTxtFileLoader

__version__ = "0.1.0"

# connect the hooks

def flaskbb_extensions(app):
    print "calling ssword:flaskbb_extensions to initialize"
    app.ssword_base = os.path.join(os.path.dirname(__file__), "data")
    ssword_loader = SimpleTxtFileLoader(app)
    ssword_loader.load()
    watching_async(app)
    pass

def flaskbb_load_migrations():
    return os.path.join(os.path.dirname(__file__), "migrations")

def flaskbb_load_translations():
    return os.path.join(os.path.dirname(__file__), "translations")

def flaskbb_load_blueprints(app):
    app.register_blueprint(ssword_bp, url_prefix="/ssword")

def flaskbb_form_new_post_save(form):
    f = SimpleDFAFilter()
    ss = f.check(form.content.data)
    if len(ss) > 0:
        tips = '内容中含有敏感词'
        raise StopNewPost(tips)
    pass

def flaskbb_form_edit_post_save(form):
    f = SimpleDFAFilter()
    ss = f.check(form.content.data)
    if len(ss) > 0:
        tips = '内容中含有敏感词'
        raise StopEditPost(tips)
    pass

def flaskbb_form_new_topic_save(form, topic):
    f = SimpleDFAFilter()
    ss_title = f.check(form.title.data)
    ss_content = f.check(form.content.data)
    if len(ss_title) > 0:
        tips = "标题"
    if len(ss_content) > 0:
        if len(tips) > 0:
            tips += "、"
        tips += "内容"
    if len(tips) > 0:
        tips += "含有敏感词"
        raise StopNewTopic(tips)
    pass

'''
def flaskbb_tpl_before_navigation():
    return render_template("ssword_navlink.html")
'''

# plugin settings
SETTINGS = {
    "path": {
        "value": "~/sswords/",
        "value_type": SettingValueType.string,
        "name": "library path",
        "description": "sensitive"
    }
}
