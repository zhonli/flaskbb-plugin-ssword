# -*- coding: utf-8 -*-

class BaseFilter():
    def __init__(self):
        pass

    @classmethod
    @abstractmethod
    def build():
        pass

    @abstractmethod
    def filter(self, message, repl="*"):
        pass
