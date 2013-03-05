# -*- coding: utf8 -*-
from django.db import models

# Create your models here.
from mongoengine import *
from wikiSpider.models import *

class Item(Document):
    '''
    store the item info
    '''
    title = StringField(max_length=50,required=True,unique=True)
    summary = StringField(max_length=500)
    content = StringField(max_length=5000,required=True)
    #problem
    #cate

class Category(Document):
    '''
    store the cate info
    '''
    cate_name = StringField(max_length=50,required=True,unique=True)
    item_list = ListField(ReferenceField(Item))

def del_cate_item_DB():
    '''
    DEL cata&item DB

    WARNING:
    ALL DATA WILL DELETE!!
    '''
    Item.drop_collection()
    Category.drop_collection()


def add_cate(cate_name):
    '''
    add new cate

    @retrun True/False
    '''
    try:
        Category(cate_name=cate_name,item_list=[]).save()
        return True
    except:
        return False

def del_cate(cate_name):
    '''
    del cate

    @retrun True/False
    '''
    try:
        Category.objects(cate_name=cate_name)[0].delete()
        return True
    except:
        return False

def add_item(item_title, item_summary, item_content, cate_name):
    '''
    add new cate

    @retrun True/False
    '''
    try:
        item = Item(title=item_title, summary=item_summary, content=item_content)
        item.save()
        cate = Category.objects(cate_name=cate_name)[0]
        cate.item_list.append(item)
        cate.save()
        return True
    except:
        return False

catelist = [u'体育',u'军事']

def init_cate_item(catelist):
    '''
    init the cate
    '''
    [add_cate(name) for name in catelist]

def get_all_category():
    '''
    get all cate

    @return list

    @example
        catelist = get_all_category()
        for cate in catelist:
            print cate
    '''
    return [cate.cate_name for cate in Category.objects()]

def search_cate_items(cate_id):
    '''
    '''
    pass

def usr_get_item(item_id):
    pass

def update_usr_behavior(usr_name, cate_id, offset):
    pass
   

def get_item_cate(item_id):
    pass
def get_problem_by_item(item_id):
    pass

def get_problem_by_cate(cate_id):
    pass
def get_problem_ralation_info(prob_id):
    pass
