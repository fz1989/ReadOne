#! /usr/bin/env python
#coding=utf-8
from django.http import HttpResponse, Http404
import json
def get_all_user_info():
    return json.dumps({
        'fz':{'user_name':'fz', 'score':256, 'user_pic_idx':1},
        'dc':{'user_name':'dc', 'score':250, 'user_pic_idx':2},
        'wl':{'user_name':'wl', 'score':243, 'user_pic_idx':3},
        'zmy':{'user_name':'zmy', 'score':275,'user_pic_idx':4},
        'fz1':{'user_name':'fz', 'score':256, 'user_pic_idx':1},
        'dc1':{'user_name':'dc', 'score':270, 'user_pic_idx':2},
        'wl1':{'user_name':'wl', 'score':253, 'user_pic_idx':3},
        'zmy1':{'user_name':'zmy', 'score':285,'user_pic_idx':4},
        'fz2':{'user_name':'fz', 'score':256, 'user_pic_idx':1},
        'dc2':{'user_name':'dc', 'score':250, 'user_pic_idx':2},
        'wl2':{'user_name':'wl', 'score':263, 'user_pic_idx':3},
        'zmy2':{'user_name':'zmy', 'score':257,'user_pic_idx':4}

                    })
def get_user_arch(user_id):
    return [
            {'arch_id': u'打败丧尸', 'arch_score': 5},
            {'arch_id': u'击败狄仁杰', 'arch_score': 15},
            {'arch_id': u'躲猫猫', 'arch_score': 25},
            {'arch_id': u'猜不到我', 'arch_score': 35},
            {'arch_id': u'怒被雷劈300回', 'arch_score': 15},
            {'arch_id': u'重新来过', 'arch_score': 115},
            {'arch_id': u'卖萌可耻', 'arch_score': 35}
        ]

def rank(request):
    if request.method == 'POST':
        if 'user_id' in request.POST:
            user_id = request.POST['user_id']
            user_dict_info = json.loads(get_all_user_info())
            list_all_rank = {}
            for key in user_dict_info.keys():
                list_all_rank[key] = user_dict_info[key]['score']
            sorted_rank =  sorted(list_all_rank.items(), key=lambda list_all_rank: list_all_rank[1])
            sorted_rank.reverse()
            if len(sorted_rank) > 10:
                sorted_rank = sorted_rank[0:10]
            response = []
            for user_id, user_score in sorted_rank:
                unit_dict = {}
                unit_dict['user_id'] = user_id
                unit_dict['score'] = user_score
                unit_dict['user_pic_idx'] = user_dict_info[user_id]['user_pic_idx']
                response.append(unit_dict)
            return HttpResponse(json.dumps({'response':response}))
        else:
            raise Http404()
    else:
        raise Http404()

def arch_rank(request):
    if request.method == 'POST':
        if 'user_id' in request.POST:
            user_id = request.POST['user_id']
            response = get_user_arch(user_id)
            return HttpResponse(json.dumps({'response' : response}))
        else:
            raise Http404()
    else:
        raise Http404()
