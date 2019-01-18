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

    def on_moved(self, event):
        if event.is_directory:
            print "directory moved from {0} to {1}".format(event.src_path, event.dest_path)
        else:
            print "file moved from {0} to {1}".format(event.src_path, event.dest_path)

    def on_created(self, event):
        if event.is_directory:
            print "directory created:{0}".format(event.src_path)
            with self.app.app_context():
                current_app.keyword_chains = {}
            self.fileLoader.load_async()
        else:
            print "file created:{0}".format(event.src_path)

    def on_deleted(self, event):
        if event.is_directory:
            print "directory deleted:{0}".format(event.src_path)
        else:
            print "file deleted:{0}".format(event.src_path)

        with self.app.app_context():
            current_app.keyword_chains = {}
        self.fileLoader.load_async()

    def on_modified(self, event):
        if event.is_directory:
            print "directory modified:{0}".format(event.src_path)
        else:
            print "file modified:{0}".format(event.src_path)
            with self.app.app_context():
                current_app.keyword_chains = {}
            self.fileLoader.load_async()
