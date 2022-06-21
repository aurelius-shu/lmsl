#!/usr/bin/env python3
# -*- coding:utf-8 -*-
'''
Factory Method
'''


class ChinaGetter:
    def __init__(self):
        self.trans = dict(dog=u'小狗', cat=u'小猫')

    def get(self, msgid):
        try:
            return self.trans[msgid]
        except KeyError:
            return str(msgid)


class EnglishGetter:
    def get(self, msgid):
        return str(msgid)


def get_localizer(language='English'):
    languages = dict(English=EnglishGetter, China=ChinaGetter)
    return languages[language]()


if __name__ == '__main__':
    e, g = get_localizer('English'), get_localizer('China')
    for msgid in 'dog parrot cat bear'.split():
        print(e.get(msgid), g.get(msgid))
