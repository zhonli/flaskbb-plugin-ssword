# -*- coding: utf-8 -*-
from abc import ABCMeta, abstractmethod


class BaseLoader():
    __metaclass__ = ABCMeta

    def __init__(self):
         pass


class BaseFileLoader(BaseLoader):
    def __init__(self, app):
        super(BaseFileLoader, self).__init__()
        self.app = app

    @abstractmethod
    def load(self):
        pass

    @abstractmethod
    def load_async(self):
        pass
