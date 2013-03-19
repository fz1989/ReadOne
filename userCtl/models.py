from django.db import models

# Create your models here.
from mongoengine import *
from random import *

class User(Document):
    '''
    store all user info
    '''
    name = StringField(max_length=50,required=True,unique=True)
    pwd = StringField(max_length=50,required=True)
    follower = ListField(ReferenceField('User'))
    rank = IntField(default=0)
    quality = DictField()   # for cate
    history = DictField()   # for item
    archive = DictField()

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

    @return (name,pwd,follower_name_list,rank,history,quality,archive,pic_index)/None
    '''
    try:
        user = User.objects(name=name)[0]
        return user.name, user.pwd, [u.name for u in user.follower],\
            user.rank, user.history.keys(), user.quality, user.archive,\
            randint(1,8)
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

def set_pwd(name, pwd):
    '''
    set user pwd
    @return True/False
    '''
    try:
        user = User.objects(name=name)[0]
        user.pwd = pwd
        user.save()
        return True
    except:
        return False

def get_pwd(name):
    '''
    get user pwd
    @return pwd/None
    '''
    try:
        user = User.objects(name=name)[0]
        return user.pwd
    except:
        return None

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

def set_rank(name,rank):
    '''
    set rank
    @return True/False
    '''
    try:
        user = User.objects(name=name)[0]
        user.rank = rank
        user.save()
        return True
    except:
        return False

def get_rank(name):
    '''
    get rank
    @return rank/None
    '''
    try:
        user = User.objects(name=name)[0]
        return user.rank
    except:
        return None

def set_quality(user_name,cate_name,quality):
    '''
    set quality to cate_name
    @return True/False
    '''
    try:
        user = User.objects(name=user_name)[0]
        user.quality[cate_name] = quality
        user.save()
        return True
    except:
        return False

def get_quality(user_name,cate_name):
    '''
    get user's cate_name quality
    @return quality/None
    '''
    try:
        user = User.objects(name=user_name)[0]
        return user.quality[cate_name]
    except:
        return None

def set_history(user_name,item_name,history):
    '''
    set history to item_name
    @return True/False
    '''
    try:
        user = User.objects(name=user_name)[0]
        user.history[item_name] = history
        user.save()
        return True
    except:
        return False

def get_history(user_name,item_name):
    '''
    get user's item history
    @return history/None
    '''
    try:
        user = User.objects(name=user_name)[0]
        return user.history[item_name]
    except:
        return None

def set_archive(user_name,arch_name,arch_score):
    '''
    set user's arch
    @return True/False
    '''
    try:
        user = User.objects(name=user_name)[0]
        user.archive[arch_name] = arch_score
        user.save()
        return True
    except:
        return False

def get_archive(user_name,arch_name):
    '''
    get user's archive
    @return arch_score/None
    '''
    try:
        user = User.objects(name=user_name)[0]
        return user.archive[arch_name]
    except:
        return None

