from django.db import models

# Create your models here.
from mongoengine import *

class User(Document):
    userName = StringField(max_length=50,required=True,unique=True)
    userPw = StringField(max_length=50,required=True)

def delUserDB():
    '''
    DEL User DB

    WARNING:
    ALL USER DATA WILL DELETE!!
    '''
    User.drop_collection()

def regUser(name,password):
    '''
    reg user
    return True/False
    '''
    try:
        User(userName=name,userPw=password).save()
        return True
    except:
        return False

def delUser(name):
    '''
    del the user
    '''
    User.objects(userName=name).delete()
    return True

def addFriend(name1,name2):
    pass




