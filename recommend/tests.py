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

        usr_recom = recommend('fz')
        item_list = usr_recom.get_recommend_items()
        print item_list
        self.assertEqual(sorted([1,2,3,4,5,6,13,14,15,16]), sorted(item_list))

    def test_usrCF_recommend(self):

        usr_recom = recommend('dc')
        item_list = usr_recom.get_recommend_items()
        print item_list
        self.assertEqual(sorted([3, 4, 5, 6, 10, 11, 12, 14, 15, 16]), sorted(item_list))

