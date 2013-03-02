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

    def test_post_search_all(self):
        self.client = Client()
        response = self.client.post('/friends/', {'action':'search','usr_id':''})
        self.assertEqual(response.content, json.dumps([ {'userid':'di ren jie', 'score':'3600','achienemwnt':'ji bai bike damo wang','picture':'hello python'},
                        {'userid':'cao sang shi', 'score':'3600','achienemwnt':'ji bai bike damo wang','picture':'hello python'}
                    ]))

    def test_post_search_one(self):
        self.client = Client()
        response = self.client.post('/friends/', {'action':'search','usr_id':'12'})
        self.assertEqual(response.content, json.dumps({'username':123, 'score':'3600', 'achienemwnt':'ji bai bike damo wang','picture':'hello python'}))
