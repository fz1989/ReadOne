#! /usr/bin/env python
#coding=utf-8
from django.http import HttpResponse, Http404
from userCtl.models import *
from itemCtl.models import *
import json
def get_all_user_info():
    ret = {}
    user_name_list = get_all_user_name()
    for user_name in user_name_list:
        user_info = get_user(user_name)
        ret[user_info[0]] = {'user_name': user_info[0], 'score': user_info[3], 'user_pic_idx':
                user_info[7]}

def get_user_arch(user_id):
    ret = []
    user_arch_dict = get_user(user_id)[6]
    for keys in user_arch_dict.keys():
        ret.append({'arch_id': keys, 'arch_score': user_arch_dict[keys]})
    return ret

def rank(request):
    if request.method == 'POST':
        if 'user_id' in request.POST:
            user_id = request.POST['user_id']
            user_dict_info = get_all_user_info()
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
