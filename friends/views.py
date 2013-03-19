#! /usr/bin/env python
#coding=utf-8
from django.http import HttpResponse, Http404
from userCtl.models import *
from itemCtl.models import *
import json

def get_all_friends(user_id):
    ret = []
    friends_list = get_user(user_id)[2]
    for friends_id in friends_list:
        if get_follow(friends_id, user_id):
            friends_info = get_user(friends_id)
            ret.append({'user_pic_idx': friends_info[7],'user_id': friends_info[0]})
    return ret


def get_user_info(user_id):
    user_info = get_user(user_id)
    return {'user_id': user_info[0], 'user_pic_idx': user_info[7]}


def update_follow_friends(user_id, friends_id):
    add_follow(user_id, friends_id)


def follow_friends(request):
    if request.method == 'POST':
        if 'user_id' in request.POST and 'friends_id' in request.POST:
            user_id = request.POST['user_id']
            friends_id = request.POST['friends_id']
            update_follow_friends(user_id, friends_id)
            return HttpResponse('YES')
        else:
            raise Http404()
    else:
        raise Http404()


def search_friends(request):
    response = None
    if request.method == 'POST':
        if 'user_id' in request.POST:
            user_id = request.POST['user_id']
            response = get_user_info(user_id)
            return HttpResponse(json.dumps(response))
        else:
            raise Http404()
    else:
        raise Http404()


def show_friends(request):
    if request.method == 'POST':
        if 'user_id' in request.POST:
            user_id = request.POST['user_id']
            response = get_all_friends(user_id)
            return HttpResponse(json.dumps({'response': response}))
        else:
            raise Http404()
    else:
        raise Http404()
