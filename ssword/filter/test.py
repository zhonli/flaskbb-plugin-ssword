#!/usr/bin/env python
# -*- coding:utf-8 -*-

from . import DFAFilter, BSFilter, NaiveFilter

def test_first_character():
    gfw = DFAFilter()
    gfw.add("1989年")
    assert gfw.filter("1989", "*") == "1989"


if __name__ == "__main__":
    # gfw = NaiveFilter()
    # gfw = BSFilter()
    gfw = DFAFilter()
    gfw.parse("keywords")
    import time
    t = time.time()
    print gfw.filter("法轮功 我操操操", "*")
    print gfw.filter("针孔摄像机 我操操操", "*")
    print gfw.filter("售假人民币 我操操操", "*")
    print gfw.filter("传世私服 我操操操", "*")
    print time.time() - t

    test_first_character()
