#! /usr/bin/env python
#coding=utf-8
from django.core.management import setup_environ
import os
import sys

def add():
    add_user('fz', '123456')
    add_user('dc', '123456')
    add_user('wl', '123456')
    add_user('zmy', '123456')


if __name__ == '__main__':
    os.environ.setdefault("DJANGO_SETTINGS_MODULE", "ReadOneServer.settings")
    from django.core.management import execute_from_command_line
    from userCtl.models import *
    from itemCtl.models import *
    add()
    print 'hello'
