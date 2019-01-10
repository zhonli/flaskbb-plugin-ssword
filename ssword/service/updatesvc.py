# -*- coding:utf-8 -*-
import os
from watchdog.events import FileSystemEventHandler
from flask import current_app
from ..loader.txtFileLoader import SimpleTxtFileLoader

class UpdateService(FileSystemEventHandler):
    def __init__(self, app = None):
        FileSystemEventHandler.__init__(self)
        self.app = app
        with self.app.app_context():
            if not current_app.ssword_base:
                raise Exception("can't find the ssword_base in current_app")
            self.fileLoader = SimpleTxtFileLoader(current_app.ssword_base)

    def on_moved(self, event):
        if event.is_directory:
            print "directory moved from {0} to {1}".format(event.src_path, event.dest_path)
        else:
            print "file moved from {0} to {1}".format(event.src_path, event.dest_path)

    def on_created(self, event):
        if event.is_directory:
            print "directory created:{0}".format(event.src_path)
        else:
            print "file created:{0}".format(event.src_path)

    def on_deleted(self, event):
        if event.is_directory:
            print "directory deleted:{0}".format(event.src_path)
        else:
            print "file deleted:{0}".format(event.src_path)

    def on_modified(self, event):
        if event.is_directory:
            print "directory modified:{0}".format(event.src_path)
        else:
            print "file modified:{0}".format(event.src_path)

        with self.app.app_context():
            current_app.keyword_chains = None
            current_app.sswords = self.fileLoader.load()


def to_sslib_path(ospath):
    sslib_path = ospath
    return sslib_path
