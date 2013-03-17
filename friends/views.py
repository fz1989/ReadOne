#! /user/bin/env python
#coding=utf-8
from django.http import HttpResponse, Http404
import json

user_list = ["a","b","c","d"]
def get_all_user_info():
    return json.dumps({
        'fz':{'user_id': 'fz', 'score': 3600,'arch': u'正直','user_pic_idx': 1},
        'dc':{'user_id': 'dc', 'score': 3600,'arch': u'卖萌','user_pic_idx': 1},
                      })

def get_all_friends(user_id):
    return [
            {'user_pic_idx': 1, 'user_id': u'狄仁杰'},
            {'user_pic_idx': 2, 'user_id': u'狄杰仁'},
            {'user_pic_idx': 3, 'user_id': u'仁杰狄'},
            {'user_pic_idx': 4, 'user_id': u'仁狄杰'},
            {'user_pic_idx': 5, 'user_id': u'杰仁狄'},
            {'user_pic_idx': 6, 'user_id': u'杰狄人'}
            ]

def get_user_info(user_id):
    
    return {'user_id': 'fz', 'user_pic_idx': 1}

def update_follow_friends(user_id, friends_id):
    pass

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
