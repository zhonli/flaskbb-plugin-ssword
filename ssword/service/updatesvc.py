# -*- coding:utf-8 -*-
import os
from watchdog.events import FileSystemEventHandler
from flask import current_app
from ..loader.txtFileLoader import SimpleTxtFileLoader

class UpdateService(FileSystemEventHandler):
    def __init__(self):
        FileSystemEventHandler.__init__(self)
        self.fileLoader = SimpleTxtFileLoader()

    def on_moved(self, event):
        if event.is_directory:
            print "directory moved from {0} to {1}".format(event.src_path,event.dest_path)
        else:
            print "file moved from {0} to {1}".format(event.src_path,event.dest_path)

    def on_created(self, event):
        if event.is_directory:
            print "directory created:{0}".format(event.src_path)
        else:
            sslib_path = self.get_sslib_path(event.src_path)
            current_app.cache[sslib_path] = self.fileLoader.load(event.src_path)
            print "file created:{0}".format(event.src_path)

    def on_deleted(self, event):
        if event.is_directory:
            for parent, dirnames, fnames in os.walk(event.src_path):
                for fname in fnames:
                    txt_path = os.path.join(parent, fname)
                    if os.path.splitext(txt_path)[1] == ".txt":
                        sslib_path = self.get_sslib_path(txt_path)
                        current_app.cache.delete(sslib_path)
            print "directory deleted:{0}".format(event.src_path)
        else:
            sslib_path = self.get_sslib_path(even.src_path)
            current_app.cache.delete(sslib_path)
            print "file deleted:{0}".format(event.src_path)

    def on_modified(self, event):
        if event.is_directory:
            print "directory modified:{0}".format(event.src_path)
        else:
            sslib_path = self.get_sslib_path(event.src_path)

            current_app.cache.set(sslib_path,
            print "file modified:{0}".format(event.src_path)

    def get_sslib_path(self, path):
        sslib_path = path
        return sslib_path
