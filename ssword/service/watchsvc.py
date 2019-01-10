# -*- coding: utf-8 -*-

import os
from watchdog.observers import Observer
# import time
from .updatesvc import UpdateService
from flask import current_app

def watching_async(app):
    observer = Observer()
    updatesvc = UpdateService(app)
    with app.app_context():
        if not current_app.ssword_base:
            raise Exception("can't find the ssword_base in current_app")
        observer.schedule(updatesvc, current_app.ssword_base, True)
    observer.start()
    '''
    try:
        while True:
            time.sleep(1)
    except KeyboardInterrupt:
        observer.stop()
    observer.join()
    '''
