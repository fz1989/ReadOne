"""
This file demonstrates writing tests using the unittest module. These will pass
when you run "manage.py test".

Replace this with more appropriate tests for your application.
"""

from django.test import TestCase
from django.test.client import Client

class SimpleTest(TestCase):
    def test_basic_addition(self):
        """
        Tests that 1 + 1 always equals 2.
        """
        self.assertEqual(1 + 1, 2)

    def test_flogin(self):
        self.client = Client()
        response = self.client.post('/login/', {'user_id':'sdsd','user_pwd':'sdsdaaa'})
        print response.content
        self.assertEqual(response.content, "NO")

    def test_sflogin(self):
        self.client = Client()
        response = self.client.post('/login/', {'user_id':'dc','user_pwd':'123456'})
        print response.content
        self.assertEqual(response.content, "YES")
