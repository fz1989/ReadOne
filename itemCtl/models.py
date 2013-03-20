# -*- coding: utf8 -*-
from django.db import models

# Create your models here.
from mongoengine import *
from wikiSpider.models import *
from random import *

class Problem(Document):
    '''
    store problem
    '''
    ref_item = ReferenceField('Item')
    question = StringField(max_length=500, required=True, unique=True, unique_with='ref_item')
    answer = DictField()
    correct = StringField(max_length=10)

class Item(Document):
    '''
    store the item info
    '''
    title = StringField(max_length=100, required=True, unique=True)
    sub_title = StringField(max_length=200)
    pic_index = IntField()
    summary = StringField(max_length=500)
    content = StringField(max_length=5000, required=True)
    problem = ListField(ReferenceField(Problem))
    cate = ReferenceField('Category')

class Category(Document):
    '''
    store the cate info
    '''
    cate_name = StringField(max_length=50, required=True, unique=True)
    item_list = ListField(ReferenceField(Item))

def add_cate(cate_name):
    '''
    add new cate

    @retrun True/False
    '''
    try:
        Category(cate_name=cate_name, item_list=[]).save()
        return True
    except:
        return False

def get_cate(cate_name):
    '''
    get cate info from name

    @return (cate_name,item_title_list)/None
    '''
    try:
        cate = Category.objects(cate_name=cate_name)[0]
        return cate.cate_name, [item.title for item in cate.item_list]
    except:
        return None

def get_all_cate_name():
    '''
    get all cate name

    @return list

    @example
        catelist = get_all_category()
        for cate in catelist:
            print cate
    '''
    return [cate.cate_name for cate in Category.objects()]

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

def add_item(item_title, item_sub_title, pic_index, item_summary, item_content, cate_name):
    '''
    add new cate

    @retrun True/False
    '''
    try:
        cate = Category.objects(cate_name=cate_name)[0]
        item = Item(title=item_title, sub_title=item_sub_title, pic_index = pic_index, summary=item_summary, \
            content=item_content,cate=cate)
        item.save()
        cate.item_list.append(item)
        cate.save()
        return True
    except:
        return False

def get_item(item_title):
    '''
    get item info from title

    @return (title,pic_index,summary,content,problem_question_list,cate_name,sub_title,id)/None
    '''
    try:
        item = Item.objects(title=item_title)[0] 
        return item.title, item.pic_index, item.summary, item.content,\
                [prob.question for prob in item.problem], item.cate.cate_name,\
                item.sub_title,str(item.id)
    except:
        return None

def get_item_by_id(item_id):
    '''
    get item name from id

    @return (title,pic_index,summary,content,problem_question_list,cate_name,sub_title,id)/None
    '''
    try:
        item = Item.objects(id=item_id)[0] 
        return item.title, item.pic_index, item.summary, item.content,\
                [prob.question for prob in item.problem], item.cate.cate_name,\
                item.sub_title,str(item.id)
    except:
        return None

def set_content(item_title, content):
    '''
    set content
    @return True/False
    '''
    try:
        item = Item.objects(title=item_title)[0] 
        item.content = content
        item.save()
        return True
    except:
        return False
    

def del_item(item_title):
    '''
    del item by title

    @retrun True/False
    '''
    try:
        Item.objects(title=item_title)[0].delete()
        return True
    except:
        return False

def add_prob(item_title, question, answer, correct):
    '''
    add problem

    @item_title:str
    @question:str
    @answer:dict
    @correct:str

    @return:True/False
    '''
    try:
        item = Item.objects(title=item_title)[0]
        prob = Problem(ref_item=item, question=question, answer=answer, correct=correct)
        prob.save()
        item.problem.append(prob)
        item.save()
        return True
    except:
        return False

def get_prob(ref_item_title,question):
    '''
    get prob info

    @return ref_item_title,question,answer_dict,correct
    '''
    try:
        item = Item.objects(title=ref_item_title)[0]
        prob = Problem.objects(ref_item=item,question=question)[0]
        return prob.ref_item.title, prob.question, prob.answer, prob.correct
    except:
        return None
    
def del_prob(item_title,question):
    '''
    del prob by item title,question

    @return:True/False
    '''
    try:
        item = Item.objects(title=item_title)[0]
        Problem.objects(ref_item=item, question=question)[0].delete()
        return True
    except:
        return False

#########################################################
#   logic fun                                           #
#########################################################

def del_cate_item_prob_DB():
    '''
    DEL cata&item DB

    WARNING:
    ALL DATA WILL DELETE!!
    '''
    Item.drop_collection()
    Category.drop_collection()
    Problem.drop_collection()

def init_cate_item(catelist):
    '''
    init the cate

    @ return True/False
    ''' 
    try:
        for name in catelist:
            assert add_cate(name)
        return True
    except:
        return False

