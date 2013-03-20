#!/usr/bin/env python
#coding=utf-8
"""
This file demonstrates writing tests using the unittest module. These will pass
when you run "manage.py test".

Replace this with more appropriate tests for your application.
"""

from django.http import HttpResponse, Http404
from django.test import TestCase
from django.test.client import Client
from itemCtl.models import *
from userCtl.models import *
import json

class SimpleTest(TestCase):
    def test_basic_addition(self):
        """
        Tests that 1 + 1 always equals 2.
        """
        self.assertEqual(1 + 1, 2)

    def test_cate_function(self):
        self.client = Client()
        response = self.client.get('/cate/')

    def test_items_recommend(self):
        print 'test_recom'
        self.client = Client()
        response = self.client.post('/recommend/', {'user_id':'fz'})
        print json.loads(response.content)

    def test_items(self):
        print "test_items"
        self.client = Client()
        response = self.client.post('/items/', {'user_id': 'fz', 'item_id': u'5149a7df18228537058bf7cb'})
        print json.loads(response.content)

    def test_edit(self):
        print "test_edit"
        all_cate_name = get_all_cate_name()
        print 'all_cate_name %s' % all_cate_name
        for cate_name in all_cate_name:
            cate_info = get_cate(cate_name)
            print 'cate_info', cate_info
           # for item_name in cate_info[1]:
           #     item_info = get_item(item_name)
           #     print 'item_info', item_info
           #     for prob_question in item_info[3]:
           #         prob_info = get_prob(item_info[0],prob_question)
           #         print 'prob_info', prob_info
        #self.client = Client()
       # response = self.client.post('/items/edit/', {'user_id': 'fz', 'item_id':'1', 'text':'aaaa'})
       # print response.content
