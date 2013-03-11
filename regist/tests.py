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
        response = self.client.post('/regist/', {'usr_id':'fz', 'usr_pwd':'123'})
        print response.content
        self.assertEqual('YES', response.content)


