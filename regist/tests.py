"""
This file demonstrates writing tests using the unittest module. These will pass
when you run "manage.py test".

Replace this with more appropriate tests for your application.
"""

from django.test import TestCase
from django.http import HttpResponse
from django.test.client import Client

class SimpleTest(TestCase):
    def test_basic_addition(self):
        """
        Tests that 1 + 1 always equals 2.
        """
        self.assertEqual(1 + 1, 2)

    def test_basic_regist(self):
        self.client = Client()
        response = self.client.post('/regist/', {'user_id':'dc2', 'user_pwd':'jiumaimeng'})
        print response.content
        self.assertEqual('NO', response.content)

    def test_rbasic_regist(self):
        self.client = Client()
        response = self.client.post('/regist/', {'user_id':'dc', 'user_pwd':'jiumaimeng'})
        print response.content
        self.assertEqual('NO', response.content)


