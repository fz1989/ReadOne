#! /usr/bin/env python
#coding=utf-8
from django.core.management import setup_environ
from userSettings import *
import os
import sys

def add():
    delUserDB()
    for user_id in user_list:
        add_user(user_id, '123456')

    for user_id in user_score.keys():
        set_rank(user_id, user_score[user_id])

    for user_id in user_arch.keys():
        for arch_name in user_arch[user_id].keys():
            set_archive(user_id, arch_name, user_arch[user_id][arch_name])

    for user_id in user_follow.keys():
        for other in user_follow[user_id]:
            add_follow(user_id, other)

    for user_id in user_history.keys():

        for cate_id in cate_list:
            set_quality(user_id, cate_id, 0)
            print cate_id

        for history_name in user_history[user_id]:
            set_history(user_id, history_name, 1)
            print history_name
            print get_item(history_name)[5]
            num = get_quality(user_id, get_item(history_name)[5])
            num += 1
            set_quality(user_id, get_item(history_name)[5], num)

if __name__ == '__main__':
    os.environ.setdefault("DJANGO_SETTINGS_MODULE", "ReadOneServer.settings")
    from django.core.management import execute_from_command_line
    from userCtl.models import *
    from itemCtl.models import *
    add()
    print 'hello'
