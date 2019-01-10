# -*- coding: utf-8 -*-
from abc import ABCMeta, abstractmethod

class BaseFilter():
    __metaclass__ = ABCMeta
    def __init__(self):
        pass

    @abstractmethod
    def filter(self, message, repl="*"):
        pass
