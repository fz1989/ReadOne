# -*- coding: utf8 -*- 
"""
This file demonstrates writing tests using the unittest module. These will pass
when you run "manage.py test".

Replace this with more appropriate tests for your application.
"""

from django.test import TestCase
from models import *
from random import *
catelist = [u'体育',u'军事']

class CategoryTest(TestCase):

    def test_add_cate(self):
        del_cate_item_prob_DB()
        self.assertTrue(add_cate(u'体育'))
        self.assertFalse(add_cate(u'体育'))

    def test_get_cate(self):
        del_cate_item_prob_DB()
        self.assertTrue(add_cate(u'体育'))
        self.assertIsNotNone(get_cate(u'体育'))
        self.assertIsNone(get_cate(u'科技'))

    def test_del_cate(self):
        del_cate_item_prob_DB()
        self.assertTrue(add_cate(u'体育'))
        self.assertTrue(del_cate(u'体育'))
        self.assertFalse(del_cate(u'体育'))

    def test_init__get_all_cate_item(self):
        del_cate_item_prob_DB()
        self.assertTrue(init_cate_item(catelist))
        self.assertEqual(catelist,get_all_cate_name())
        
class ItemTest(TestCase):
    def test_add_item(self):
        del_cate_item_prob_DB()
        self.assertTrue(init_cate_item(catelist))
        self.assertTrue(add_item(u'足球',u's',1,u'简介',u'正文',catelist[0]))
        self.assertFalse(add_item(u'足球',u's',2,u'简介',u'正文',catelist[0]))
        self.assertFalse(add_item(u'足球',u's',3,u'简介',u'正文',catelist[1]))

    def test_get_item_id(self):
        del_cate_item_prob_DB()
        self.assertTrue(init_cate_item(catelist))
        self.assertTrue(add_item(u'足球',u's',1,u'简介',u'正文',catelist[0]))
        self.assertIsNotNone(get_item(u'足球'))
        self.assertIsNone(get_item(u'篮球'))

    def test_del_item(self):
        del_cate_item_prob_DB()
        self.assertTrue(init_cate_item(catelist))
        self.assertTrue(add_item(u'足球',u's',1,u'简介',u'正文',catelist[0]))
        self.assertTrue(del_item(u'足球'))
        self.assertFalse(del_item(u'足球'))

    def test_set_content(self):
        del_cate_item_prob_DB()
        self.assertTrue(init_cate_item(catelist))
        self.assertTrue(add_item(u'足球',u's',1,u'简介',u'正文',catelist[0]))
        self.assertTrue(set_content(u'足球',u'正文1111111111111'))

class ProblemTest(TestCase):
    def test_add_prob(self):
        del_cate_item_prob_DB()
        self.assertTrue(init_cate_item(catelist))
        self.assertTrue(add_item(u'足球',u's',1,u'简介',u'正文',catelist[0]))
        self.assertTrue(add_item(u'篮球',u's',1,u'简介',u'正文',catelist[0]))
        self.assertTrue(add_prob(u'足球',u'问题1',{'A':'11','B':'22','C':'33'},'A'))
        self.assertTrue(add_prob(u'足球',u'问题2',{'A':'11','B':'22','C':'33'},'A'))
        self.assertFalse(add_prob(u'足球',u'问题1',{'A':'11','B':'22','C':'33'},'A'))
        self.assertTrue(add_prob(u'篮球',u'问题1',{'A':'11','B':'22','C':'33'},'A'))

    def test_get_prob(self):
        del_cate_item_prob_DB()
        self.assertTrue(init_cate_item(catelist))
        self.assertTrue(add_item(u'足球',u's',1,u'简介',u'正文',catelist[0]))
        self.assertTrue(add_prob(u'足球',u'问题1',{'A':'11','B':'22','C':'33'},'A'))
        self.assertIsNotNone(get_prob(u'足球',u'问题1'))
        self.assertIsNone(get_prob(u'足球',u'问题'))

    def test_del_prob(self):
        del_cate_item_prob_DB()
        self.assertTrue(init_cate_item(catelist))
        self.assertTrue(add_item(u'足球',u's',1,u'简介',u'正文',catelist[0]))
        self.assertTrue(add_prob(u'足球',u'问题1',{'A':'11','B':'22','C':'33'},'A'))
        self.assertTrue(add_prob(u'足球',u'问题2',{'A':'11','B':'22','C':'33'},'A'))
        self.assertTrue(del_prob(u'足球',u'问题1'))
        self.assertFalse(del_prob(u'足球',u'问题1'))
        self.assertTrue(del_prob(u'足球',u'问题2'))

class ModelTest(TestCase):
    def test_whole_modle(self):
        del_cate_item_prob_DB()
        self.assertTrue(init_cate_item(['cate1','cate2']))
        
        self.assertTrue(add_item('item1',u's',1,'sum1','cont1','cate1'))
        self.assertTrue(add_item('item2',u's',1,'sum2','cont2','cate1'))
        self.assertTrue(add_item('item3',u's',1,'sum3','cont3','cate2'))
        self.assertTrue(add_item('item4',u's',1,'sum4','cont4','cate2'))

        self.assertTrue(add_prob('item1','prob1',{'A':'11','B':'22','C':'33'},'A'))
        self.assertTrue(add_prob('item1','prob2',{'A':'44','B':'55','C':'66'},'B'))
        self.assertTrue(add_prob('item2','prob1',{'A':'77','B':'88','C':'99'},'C'))

        # get all info
        all_cate_name = get_all_cate_name()
        print 'all_cate_name', all_cate_name
        for cate_name in all_cate_name:
            cate_info = get_cate(cate_name)
            print 'cate_info', cate_info
            for item_name in cate_info[1]:
                item_info = get_item(item_name)
                print 'item_info', item_info
                for prob_question in item_info[3]:
                    prob_info = get_prob(item_info[0],prob_question)
                    print 'prob_info', prob_info























