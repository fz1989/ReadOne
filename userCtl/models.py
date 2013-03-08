from django.db import models

# Create your models here.
from mongoengine import *

class User(Document):
    '''
    store all user info
    '''
    name = StringField(max_length=50,required=True,unique=True)
    pwd = StringField(max_length=50,required=True)
    follower = ListField(ReferenceField('User'))
    rank = IntField()
    history = ListField(DictField())

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
    
    @return user_name_list
    '''
    return [user.name for user in User.objects()]

def get_user(name):
    '''
    search user info

    @return (name,pwd,follower_name_list,rank,history)/None
    '''
    try:
        user = User.objects(name=name)[0] 
        return user.name, user.pwd, [follower.name for follower in user.follower],\
            user.rank, user.history
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

def add_follow(name1,name2):
    '''
    name1 follow name2

    @return:True/False
    '''
    try:
        user1 = User.objects(name=name1)[0]
        user2 = User.objects(name=name2)[0]
        assert user2 not in user1.follower
        user1.follower.append(user2)
        user1.save()
        return True
    except:
        return False

def get_follow(name1,name2):
    '''
    get if name1 follow name2
    @return:True/False
    '''
    try:
        user1 = User.objects(name=name1)[0]
        user2 = User.objects(name=name2)[0]
        return user2 in user1.follower
    except:
        return False
    
def del_follow(name1,name2):
    '''
    name1 del follow name2
    @return True/False
    '''
    try:
        user1 = User.objects(name=name1)[0]
        user2 = User.objects(name=name2)[0]
        user1.follower.remove(user2)
        user1.save()
        return True
    except:
        return False







