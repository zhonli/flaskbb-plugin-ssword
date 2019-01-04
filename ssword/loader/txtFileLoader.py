# -*- coding:uft-8 -*-

import os
from .baseLoader import BaseFileLoader

class SimpleTxtFileLoader(BaseFileLoader):
    def __init__(self, libpath):
        super(SimpleTxtFileLoader, self).__init__(libpath)
        pass

    def load(self):
        data = {}
        for parent, dirnames, fnames in os.walk(self.libpath):
            for fname in fnames:
                txt_path = os.path.join(parent, fname)
                if os.path.splitext(txt_path)[1] == ".txt":
                    sslib_path = to_sslib_path(txt_path)
                    items = {}
                    with open(txt_path, 'r') as txt:
                        for word in txt:
                            items[word] = None

                    data[sslib_path] = items
        return data


def to_sslib_path(ospath):
    sslib_path = ospath
    return sslib_path
