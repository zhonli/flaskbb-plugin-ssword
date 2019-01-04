# -*- coding: utf-8 -*-

class BaseLoader():
    def __init__(self):
        pass


class BaseFileLoader(BaseLoader):
    def __init__(self, libpath):
         super(BaseFileLoader, self).__init__(self)
         self.libpath = libpath

    @abstractmethod
    def load(self):
        pass
