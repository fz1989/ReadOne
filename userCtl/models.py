from django.db import models

# Create your models here.
from mongoengine import *

class User(Document):
    '''
    store all user info
    '''
    name = StringField(max_length=50,required=True,unique=True)
    pwd = StringField(max_length=50,required=True)
    #follow = list(user id)
    #rank = int
    #history = list(item id)
    #cate_vector = list(int)


def delUserDB():
    '''
    DEL User DB

    WARNING:
    ALL USER DATA WILL DELETE!!
    '''
    User.drop_collection()

def add_user(name, pwd):
    '''
    reg user
    @return True/False
    '''
    try:
        User(name=name, pwd=pwd).save()
        return True
    except:
        return False

def get_all_user_name():
    '''
    get all user info
    
    @return list
        each item has name/pwd
    
    @example
        all_user = get_all_usr_info()
        for u in all_user:
            print u.usr_name,u.usr_pwd
    '''
    return [user.name for user in User.objects()]

def get_user(name):
    '''
    search user info

    @return (name,pwd)/None
    '''
    try:
        user = User.objects(name=name)[0] 
        return user.name, user.pwd
    except:
        return None


def del_user(name):
    '''
    del the user

    @return True/False
    '''
    try:
        User.objects(name=name)[0].delete()
        return True
    except:
        return False
