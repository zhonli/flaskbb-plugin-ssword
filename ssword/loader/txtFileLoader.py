# -*- coding: utf-8 -*-
import os
import threading
from .baseLoader import BaseFileLoader
from flask import current_app

class SimpleTxtFileLoader(BaseFileLoader):
    def __init__(self, app):
        super(SimpleTxtFileLoader, self).__init__(app)

    def load(self):
        data = {}
        with self.app.app_context():
            for parent, dirnames, fnames in os.walk(current_app.ssword_base):
                for fname in fnames:
                    txt_path = os.path.join(parent, fname)
                    if os.path.splitext(txt_path)[1] == ".txt":
                        sslib_path = to_sslib_path(txt_path)
                        items = {}
                        with open(txt_path, 'r') as txt:
                            for line in txt:
                                word = line.strip().rstrip(',')
                                items[word] = None

                        data[sslib_path] = items
            current_app.sswords = data

    def load_async(self):
        t = threading.Thread(target=self.load)
        t.setDaemon(True)
        t.start()

def to_sslib_path(ospath):
    sslib_path = ospath
    return sslib_path
