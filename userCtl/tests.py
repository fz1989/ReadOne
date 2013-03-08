"""
This file demonstrates writing tests using the unittest module. These will pass
when you run "manage.py test".

Replace this with more appropriate tests for your application.
"""

from django.test import TestCase
from models import *

class SimpleTest(TestCase):
    def test_add_user(self):
        delUserDB()
        self.assertTrue(add_user('dc','123456'))
        self.assertFalse(add_user('dc','123456'))
        
    def test_del_user(self):
        delUserDB()
        self.assertTrue(add_user('dc','123456'))
        self.assertTrue(del_user('dc'))
        self.assertFalse(del_user('dc'))

    def test_get_all_user(self):
        delUserDB()
        self.assertTrue(add_user('dc1','123456'))
        self.assertTrue(add_user('dc2','123456'))
        self.assertTrue(add_user('dc3','123456'))
        all_name = get_all_user_name()
        self.assertEqual(len(all_name),3)
        self.assertIn('dc1',all_name)
        self.assertIn('dc2',all_name)
        self.assertIn('dc3',all_name)

    def test_get_user(self):
        delUserDB()
        self.assertTrue(add_user('dc','123456'))
        self.assertIsNotNone(get_user('dc'))
