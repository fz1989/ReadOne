"""
This file demonstrates writing tests using the unittest module. These will pass
when you run "manage.py test".

Replace this with more appropriate tests for your application.
"""

from django.http import HttpResponse
from django.test import TestCase
from django.test.client import Client
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

    def test_subcate(self):
        print 'test_subcate'
        self.client = Client()
        response = self.client.get('/cate/sub/1212/')
        print json.loads(response.content)

    def test_items(self):
        print "test_items"
        self.client = Client()
        response = self.client.post('/items/', {'user_id': 1, 'item_id': 2})
        print json.loads(response.content)

    def test_edit(self):
        print "test_edit"
        self.client = Client()
        response = self.client.post('/items/edit/', {'user_id': 'fz', 'item_id':'1', 'text':'aaaa'})
        print response.content
