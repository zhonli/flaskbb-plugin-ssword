# -*- coding: utf-8 -*-
import os
import threading
import io
from flask import current_app

class SimpleTxtFileLoader(BaseFileLoader):
    def __init__(self, app):
        super(SimpleTxtFileLoader, self).__init__(app)
        with self.app.app_context():
            self.sslib_base = current_app.ssword_base

    def load(self):
        with self.app.app_context():
            for parent, dirnames, fnames in os.walk(current_app.ssword_base):
                for fname in fnames:
                    txt_path = os.path.join(parent, fname)
                    if os.path.splitext(txt_path)[1] == ".txt":
                        txt_sslib_path = self.as_sslib_path(txt_path)
                        sswords = {}
                        try:
                            with io.open(txt_path, 'r', encoding='utf-8') as txt:
                                for line in txt:
                                    word = line.strip().rstrip(',')
                                    sswords[word] = None
                            current_app.sswords[txt_sslib_path] = sswords
                            print '%s loaded successfully' % txt_sslib_path
                        except Exception:
                            print "%s loaded failed" % txt_sslib_path
            current_app.sswords_loaded = True

    def load_async(self):
        t = threading.Thread(target=self.load)
        t.setDaemon(True)
        t.start()

    # such as /test.txt
    def as_sslib_path(self, ospath):
        sslib_base = self.sslib_base.rstrip(os.path.sep)
        sslib_path = ospath[len(sslib_base):]
        return sslib_path
