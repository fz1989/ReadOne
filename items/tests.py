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
        self.assertEqual(response.content, json.dumps({'resopnse':[ {'cate_id':'123', 'cate_name':'snake'},
                        {'cate_id':'234', 'cate_name':'dragon'}]})

)

