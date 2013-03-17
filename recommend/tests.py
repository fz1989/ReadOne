"""
This file demonstrates writing tests using the unittest module. These will pass
when you run "manage.py test".

Replace this with more appropriate tests for your application.
"""

from django.test import TestCase
from views import recommend

class SimpleTest(TestCase):
    def test_basic_addition(self):
        """
        Tests that 1 + 1 always equals 2.
        """
        self.assertEqual(1 + 1, 2)

    def test_average_recommend(self):

        user_recom = recommend('fz')
        item_list = user_recom.get_recommend_items()
        print item_list

    def test_userCF_recommend(self):

        user_recom = recommend('dc')
        item_list = user_recom.get_recommend_items()
        print item_list

