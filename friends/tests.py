"""
This file demonstrates writing tests using the unittest module. These will pass
when you run "manage.py test".

Replace this with more appropriate tests for your application.
"""

from django.test import TestCase
from django.test.client import Client
import json

class SimpleTest(TestCase):
    def test_basic_addition(self):
        """
        Tests that 1 + 1 always equals 2.
        """
        self.assertEqual(1 + 1, 2)

    def test_post_search(self):
        self.client = Client()
        response = self.client.post('/friends/search/', {'usr_id':'sdsd'})
        print json.loads(response.content)

    def test_post_follow(self):
        self.client = Client()
        response = self.client.post('/friends/follow/', {'friends_id':'23', 'usr_id':'12'})
        print response.content

    def test_show_friends(self):
        self.client = Client()
        response = self.client.post('/friends/show/', {'usr_id':'fz'})
        print json.dumps(response.content)
