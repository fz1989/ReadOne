# Create your views here.
#!/usr/bin/env bash
from django.http import HttpResponse
import json
from recommend.views import *
from random import randint
def get_all_category():
    return {
        '1': {'cate_id':'123', 'cate_name':'snake'},
        '2': {'cate_id':'234', 'cate_name':'dragon'}
        }

def search_cate_items(cate_id):
    return ([ 
        {'item_id': cate_id * 5 % 3, 'item_pic_idx': 1, 'title':'di ren jie', 'abstract': 'cao sang shi'},
        {'item_id': cate_id * 7 % 5, 'item_pic_idx': 2, 'title':'xu chu', 'abstract':'300'}
                    ])

def update_usr_behavior(usr_id, cate_id, value):
    pass

def update_items(item_id, text):
    pass

def get_item_info(item_id):
    return [{'item_id': item_id,'item_pic_idx': int(item_id) % 8, 'title':"a" * int(item_id), 'abstract':"b" * int(item_id)}]

def get_item_content(item_id):
    return {'item_id': item_id, 'item_pic_url': 'www.duomaomao.com', 'title':'WLGQ', 'sub_title': 'sanguosha', 'text': 'lalalagaidaima'}

def get_item_cate(item_id):
    pass

def items(request):
    resopnse = None
    if request.method == 'POST':
        if 'usr_id' in request.POST and 'item_id' in request.POST:
            usr_id = request.POST['usr_id']
            item_id = request.POST['item_id']
            response = get_item_content(item_id)
            cate_id = get_item_cate(item_id)
            update_usr_behavior(usr_id, cate_id, 1)
        else:
            raise Http404()
    else:
        raise Http404()
    return HttpResponse(json.dumps(response))

def recommend_items(request):
    response = []
    if request.method == 'POST' and 'usr_id' in request.POST:
        usr_id = request.POST['usr_id']
        recom = recommend(usr_id)
        item_list = recom.get_recommend_items()
        for item_id in item_list:
            response.extend(get_item_info(item_id))
    return HttpResponse(json.dumps({'response':response}))

def cate(request):
    response = get_all_category()
    return HttpResponse(json.dumps(response))

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
        if 'usr_id' in request.POST and 'item_id' in request.POST and 'text' in request.POST:
            usr_id = request.POST['usr_id']
            item_id = request.POST['item_id'];
            text = request.POST['text']
            update_items(item_id, text)
            return HttpResponse("Edit OK!")
        else:
            raise Http404()
    else:
        raise Http404()
