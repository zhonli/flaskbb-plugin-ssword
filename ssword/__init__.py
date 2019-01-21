# -*- coding: utf-8 -*-
"""
    ssword
    ~~~~~~

    A ssword Plugin for FlaskBB.

    :copyright: (c) 2018 by zhongkui li.
    :license: BSD License, see LICENSE for more details.
"""
import os
import threading
from flask_babelplus import lazy_gettext as _

from flaskbb.forum.models import Forum
from flaskbb.forum.exceptions import StopNewPost, StopEditPost, StopNewTopic

from .service.watchsvc import watching_async
from .filter.dfaFilter import SimpleDFAFilter
from .loader.txtFileLoader import SimpleTxtFileLoader

__version__ = "0.1.0"

# connect the hooks

def flaskbb_extensions(app):
    print "calling ssword:flaskbb_extensions to initialize ssword plugin"
    app.sswords_base = os.path.join(os.path.dirname(__file__), "data")
    app.sswords = {}
    app.sswords_loaded = False
    app.keyword_chains = {}
    app.keyword_chains_build_lock = threading.Lock()

    sswords_loader = SimpleTxtFileLoader(app)
    sswords_loader.load_async()
    watching_async(app)
    pass

def flaskbb_load_migrations():
    return os.path.join(os.path.dirname(__file__), "migrations")

def flaskbb_load_translations():
    return os.path.join(os.path.dirname(__file__), "translations")

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
    tips = ""
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
