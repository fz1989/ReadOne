#! /usr/bin/env python
#coding=utf-8
from django.http import HttpResponse
import json
from recommend.views import *
from random import randint
from itemCtl.models import *
from userCtl.models import *

def search_cate_items(cate_id):
    cate_info = get_cate(cate_id)
    ret = []
    print 'cateinfo', cate_info
    for item_name in cate_info[1]:
        item_info = get_item(item_name)
        item_dict = {'item_id': item_info[0], 'item_pic_idx': item_info[1], 'title':item_info[0],
            'abstract': item_info[2]}
        ret.append(item_dict)
    return ret

def update_user_behavior(user_id, cate_id, value):
    print user_id,cate_id
    num = get_quality(user_id, cate_id)
    num += value
    set_quality(user_id, cate_id, num)


def update_items(item_id, text):
    set_content(item_id, text)

def get_item_info(item_id):
    item_info = get_item(item_id)
    item_dict = {'item_id': item_info[0], 'item_pic_idx': item_info[1], 'title':item_info[0],'abstract': item_info[2]}
    return [item_dict]

def get_item_content(item_id):
    item_info = get_item(item_id)
    return {'item_id': item_info[0], 'item_pic_url': 'www.duomaomao.com', 'title':item_info[0],'sub_title': item_info[6], 'text': item_info[3]} 

def get_item_cate(item_id):
    return get_item(item_id)[5]

def items(request):
    response = None
    if request.method == 'POST':
        if 'user_id' in request.POST and 'item_id' in request.POST:
            user_id = request.POST['user_id']
            item_id = request.POST['item_id']
            response = get_item_content(item_id)
            cate_id = get_item_cate(item_id)
            update_user_behavior(user_id, cate_id, 1)
        else:
            raise Http404()
    else:
        raise Http404()
    return HttpResponse(json.dumps(response))

def recommend_items(request):
    response = []
    if request.method == 'POST' and 'user_id' in request.POST:
        user_id = request.POST['user_id']
        recom = recommend(user_id)
        item_list = recom.get_recommend_items()
        for item_id in item_list:
            response.extend(get_item_info(item_id))
    return HttpResponse(json.dumps({'response':response}))

def cate(request):
    cate_list = get_all_cate_name()
    ret = []
    for cate_id in cate_list:
        item_list = search_cate_items(cate_id)
        idx = randint(0, len(item_list) - 1)
        ret.append(item_list[idx])
    return HttpResponse(json.dumps({'response': ret}))

def subcate(request, cate_id):
    try:
        cate_id = int(cate_id)
    except ValueError:
        raise Http404()
    response = search_cate_items(cate_id)
    idx = randint(0, len(response) - 1)
    return HttpResponse(json.dumps(response[idx]))

def edit_items(request):
    if request.method == 'POST':
        if 'user_id' in request.POST and 'item_id' in request.POST and 'text' in request.POST:
            user_id = request.POST['user_id']
            item_id = request.POST['item_id'];
            text = request.POST['text']
            if not update_items(item_id, text):
                return HttpResponse("OK")
            else:
                return HttpResponse('Error')
        else:
            raise Http404()
    else:
        raise Http404()
