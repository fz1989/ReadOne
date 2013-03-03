from django.db import models

# Create your models here.
from mongoengine import *

class User(Document):
    '''
    store all user info
    '''
    usr_name = StringField(max_length=50,required=True,unique=True)
    usr_pwd = StringField(max_length=50,required=True)

def delUserDB():
    '''
    DEL User DB

    WARNING:
    ALL USER DATA WILL DELETE!!
    '''
    User.drop_collection()

def regist_usr_account(usr_name, usr_pwd):
    '''
    reg user
    @return True/False
    '''
    try:
        User(usr_name=usr_name, usr_pwd=usr_pwd).save()
        return True
    except:
        return False

def check_usr_pwd(usr_name, usr_pwd):
    '''
    check pw
    @return True/False
    '''
    try:
        userlist = User.objects(usr_name=usr_name)
        user = userlist[0]
        if user.usr_pwd == usr_pwd:
            return True
        else:
            return False
    except:
        return False

def check_usr_exist(usr_name):
    '''
    check user exist
    @return True/False
    '''
    if User.objects(usr_name=usr_name):
        return True
    else:
        return False

def get_all_usr_info():
    '''
    get all user info
    
    @return list
        each item has name/pwd
    
    @example
        all_user = get_all_usr_info()
        for u in all_user:
            print u.usr_name,u.usr_pwd
    '''
    return User.objects()

def search_usr_info(usr_name):
    '''
    search user info

    @return userinfo/None
    
    @example
        u = search_usr_info('name')
        if u:
            print u.usr_name,u.usr_pwd
    '''
    try:
        u = User.objects(usr_name=usr_name)[0]
        return u
    except:
        return None


def del_user(usr_name):
    '''
    del the user
    '''
    User.objects(usr_name=usr_name).delete()
    return True
