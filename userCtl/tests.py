"""
This file demonstrates writing tests using the unittest module. These will pass
when you run "manage.py test".

Replace this with more appropriate tests for your application.
"""

from django.test import TestCase
from models import *

class SimpleTest(TestCase):
    def test_reg_user(self):
        delUserDB()
        self.assertTrue(regist_usr_account('dc','123456'))
        self.assertFalse(regist_usr_account('dc','123456'))
        
    def test_del_user(self):
        delUserDB()
        self.assertTrue(regist_usr_account('dc','123456'))
        self.assertTrue(del_user('dc'))

    def test_exist_user(self):
        delUserDB()
        self.assertTrue(regist_usr_account('dc','123456'))
        self.assertTrue(check_usr_exist('dc'))
        self.assertTrue(del_user('dc'))
        self.assertFalse(check_usr_exist('dc'))

    def test_check_pwd(self):
        delUserDB()
        self.assertTrue(regist_usr_account('dc','123456'))
        self.assertTrue(check_usr_pwd('dc','123456'))
        self.assertTrue(del_user('dc'))
        self.assertFalse(check_usr_pwd('dc','654321'))

    def test_get_all_user(self):
        delUserDB()
        self.assertTrue(regist_usr_account('dc1','123456'))
        self.assertTrue(regist_usr_account('dc2','123456'))
        self.assertTrue(regist_usr_account('dc3','123456'))
        all_user = get_all_usr_info()
        all_name = [u.usr_name for u in all_user]
        self.assertEqual(len(all_name),3)
        self.assertIn('dc1',all_name)
        self.assertIn('dc2',all_name)
        self.assertIn('dc3',all_name)

    def test_get_all_user(self):
        delUserDB()
        self.assertIsNone(search_usr_info('dc'))
        self.assertTrue(regist_usr_account('dc','123456'))
        self.assertIsNotNone(search_usr_info('dc'))
