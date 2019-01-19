# -*- coding:utf-8 -*-
import os
from watchdog.events import FileSystemEventHandler
from flask import current_app
from ..loader.txtFileLoader import SimpleTxtFileLoader

class UpdateService(FileSystemEventHandler):
    def __init__(self, app = None):
        FileSystemEventHandler.__init__(self)
        self.app = app
        self.fileLoader = SimpleTxtFileLoader(app)

    def on_modified(self, event):
        if event.is_directory:
            with self.app.app_context():
                if current_app.ssword_base == event.src_path:
                    return
            print 'Sensitive words library changed'
            with self.app.app_context():
                current_app.keyword_chains = {}
                current_app.sswords_loaded = False
            self.fileLoader.load_async()
