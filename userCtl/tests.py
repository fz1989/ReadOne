"""
This file demonstrates writing tests using the unittest module. These will pass
when you run "manage.py test".

Replace this with more appropriate tests for your application.
"""

from django.test import TestCase
from models import *

class SimpleTest(TestCase):
    def test_basic_addition(self):
        """
        Tests that 1 + 1 always equals 2.
        """
        self.assertEqual(1 + 1, 2)
    def test_user(self):
        delUserDB()
        self.assertEqual(True,regUser('dc','123456'))
        self.assertEqual(False,regUser('dc','123456'))
        self.assertEqual(True,delUser('dc'))


