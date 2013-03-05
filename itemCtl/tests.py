# -*- coding: utf8 -*- 
"""
This file demonstrates writing tests using the unittest module. These will pass
when you run "manage.py test".

Replace this with more appropriate tests for your application.
"""

from django.test import TestCase
from models import *

class SimpleTest(TestCase):
    catelist = [u'体育',u'军事']

    def test_add_cate(self):
        del_cate_item_DB()
        self.assertTrue(add_cate(u'体育'))
        self.assertFalse(add_cate(u'体育'))

    def test_add_cate(self):
        del_cate_item_DB()
        self.assertTrue(add_cate(u'体育'))
        self.assertTrue(del_cate(u'体育'))
        self.assertFalse(del_cate(u'体育'))

    def test_init_get_cate_item(self):
        del_cate_item_DB()
        init_cate_item(self.catelist)
        self.assertEqual(self.catelist,get_all_category())
        
    def test_add_item(self):
        del_cate_item_DB()
        init_cate_item(self.catelist)
        self.assertTrue(add_item(u'足球',u'简介',u'正文',self.catelist[0]))
        self.assertFalse(add_item(u'足球',u'简介',u'正文',self.catelist[0]))
        self.assertFalse(add_item(u'足球',u'简介',u'正文',self.catelist[1]))

