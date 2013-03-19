"""
This file demonstrates writing tests using the unittest module. These will pass
when you run "manage.py test".

Replace this with more appropriate tests for your application.
"""

from django.test import TestCase
from models import *

class UserTest(TestCase):
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

class FollowTest(TestCase):
    def test_add_follow(self):
        delUserDB()
        self.assertTrue(add_user('dc1','123456'))
        self.assertTrue(add_user('dc2','123456'))
        self.assertTrue(add_follow('dc1','dc2'))
        self.assertFalse(add_follow('dc1','dc2'))

    def test_del_follow(self):
        delUserDB()
        self.assertTrue(add_user('dc1','123456'))
        self.assertTrue(add_user('dc2','123456'))
        self.assertTrue(add_follow('dc1','dc2'))
        self.assertTrue(del_follow('dc1','dc2'))
        self.assertFalse(del_follow('dc1','dc2'))

    def test_get_follow(self):
        delUserDB()
        self.assertTrue(add_user('dc1','123456'))
        self.assertTrue(add_user('dc2','123456'))
        self.assertTrue(add_follow('dc1','dc2'))
        self.assertTrue(get_follow('dc1','dc2'))
        self.assertFalse(get_follow('dc2','dc1'))
        self.assertTrue(del_follow('dc1','dc2'))
        self.assertFalse(get_follow('dc1','dc2'))

class PWDTest(TestCase):
    def test_pwd(self):
        delUserDB()
        self.assertTrue(add_user('dc','123456'))
        self.assertTrue(set_pwd('dc','1033'))
        self.assertEqual('1033',get_pwd('dc'))

class RankTest(TestCase):
    def test_rank(self):
        delUserDB()
        self.assertTrue(add_user('dc','123456'))
        self.assertTrue(set_rank('dc',10))
        self.assertEqual(10,get_rank('dc'))
        self.assertIsNone(get_rank('dc1'))

class QualityTest(TestCase):
    def test_rank(self):
        delUserDB()
        self.assertTrue(add_user('dc','123456'))
        self.assertTrue(set_quality('dc','cate1',5))
        self.assertEqual(5,get_quality('dc','cate1'))
        self.assertTrue(set_quality('dc','cate1',5))
        self.assertEqual(5,get_quality('dc','cate1'))
        self.assertTrue(set_quality('dc','cate1',10))
        self.assertEqual(10,get_quality('dc','cate1'))


class ArchiveTest(TestCase):
    def test_archive(self):
        delUserDB()
        self.assertTrue(add_user('dc','123456'))
        self.assertTrue(set_archive('dc','arch',10))
        self.assertEqual(10,get_archive('dc','arch'))
        self.assertIsNone(get_archive('dc1','arch1'))

class HistoryTest(TestCase):
    def test_history(self):
        delUserDB()
        self.assertTrue(add_user('dc','123456'))
        self.assertTrue(set_history('dc','item1',10))
        self.assertEqual(10,get_history('dc','item1'))
        self.assertIsNone(get_archive('dc','item2'))


