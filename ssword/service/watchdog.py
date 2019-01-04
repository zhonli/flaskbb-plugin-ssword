# -*- coding:utf-8 -*-

import os
from watchdog.observers import Observer
import time
from .updatesvc import UpdateService

def watching(ctx, libpath=None):
    observer = Observer()
    updatesvc = UpdateService()
    if not libpath:
        libpath = os.path.join(os.path.dirname(os.path.dirname(__file__)), "data")
    observer.schedule(updatesvc, libpath, True)
    observer.start()
    try:
        while True:
            time.sleep(1)
    except KeyboardInterrupt:
        observer.stop()
    observer.join()
