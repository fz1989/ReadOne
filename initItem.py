#! /usr/bin/env python
#coding=utf-8
from django.core.management import setup_environ
import os
import sys
from itemSettings import *
item_dict = {u'科技': 1,
             u'生活': 2,
             u'医疗': 3,
             u'文学': 4,
             u'教育': 5,
             u'旅行': 6,
             u'新闻': 7,
             u'娱乐': 8,
             u'艺术': 9,
             u'人物': 10}
def add():
    for cate_name in cate_list:
        add_cate(cate_name)
    for item in item_list:
        print item[4]
        add_item(item[0], item[1], item_dict[item[4]], item[2], item[3],item[4])
    for prob in prob_list:
        add_prob(prob[0], prob[1], prob[2],prob[3])

if __name__ == '__main__':
    os.environ.setdefault("DJANGO_SETTINGS_MODULE", "ReadOneServer.settings")
    from django.core.management import execute_from_command_line
    from userCtl.models import *
    from itemCtl.models import *
    add()
    print 'Finish init item data'
