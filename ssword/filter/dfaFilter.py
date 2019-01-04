# -*- coding: utf-8 -*-
import BaseFilter
from flask import current_app

class SimpleDFAFilter(BaseFilter):

    '''Filter Messages from keywords

    Use DFA to keep algorithm perform constantly

    >>> f = SimpleDFAFilter()
    >>> f.add("sexy")
    >>> f.filter("hello sexy baby")
    hello **** baby
    '''

    def __init__(self):
        #self.keyword_chains = {}
        self.delimit = '\x00'

    def build():
        current_app.keyword_chains = {}
        for path, bag in current_app.sswords.items():
            for key, value in bag.items():
                add(key)
        pass

    def filter(self, message, repl="*"):
        if not isinstance(message, unicode):
            message = message.decode('utf-8')
        message = message.lower()
        ret = []
        start = 0
        while start < len(message):
            level = current_app.keyword_chains
            step_ins = 0
            for char in message[start:]:
                if char in level:
                    step_ins += 1
                    if self.delimit not in level[char]:
                        level = level[char]
                    else:
                        ret.append(repl * step_ins)
                        start += step_ins - 1
                        break
                else:
                    ret.append(message[start])
                    break
            else:
                ret.append(message[start])
            start += 1

        return ''.join(ret)


def add(keyword):
    if not isinstance(keyword, unicode):
        keyword = keyword.decode('utf-8')
    keyword = keyword.lower()
    chars = keyword.strip()
    if not chars:
        return
    level = current_app.keyword_chains
    for i in range(len(chars)):
        if chars[i] in level:
            level = level[chars[i]]
        else:
            if not isinstance(level, dict):
                break
            for j in range(i, len(chars)):
                level[chars[j]] = {}
                last_level, last_char = level, chars[j]
                level = level[chars[j]]
            last_level[last_char] = {self.delimit: 0}
            break
    if i == len(chars) - 1:
        level[self.delimit] = 0
