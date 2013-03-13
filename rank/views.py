# Create your views here.
#!/usr/bin/env bash
from django.http import HttpResponse, Http404
import json
def get_all_usr_info():
    return json.dumps({
        'fz':{'usr_name':'fz', 'score':256, 'usr_pic_idx':1},
        'dc':{'usr_name':'dc', 'score':250, 'usr_pic_idx':2},
        'wl':{'usr_name':'wl', 'score':243, 'usr_pic_idx':3},
        'zmy':{'usr_name':'zmy', 'score':275,'usr_pic_idx':4},
        'fz1':{'usr_name':'fz', 'score':256, 'usr_pic_idx':1},
        'dc1':{'usr_name':'dc', 'score':270, 'usr_pic_idx':2},
        'wl1':{'usr_name':'wl', 'score':253, 'usr_pic_idx':3},
        'zmy1':{'usr_name':'zmy', 'score':285,'usr_pic_idx':4},
        'fz2':{'usr_name':'fz', 'score':256, 'usr_pic_idx':1},
        'dc2':{'usr_name':'dc', 'score':250, 'usr_pic_idx':2},
        'wl2':{'usr_name':'wl', 'score':263, 'usr_pic_idx':3},
        'zmy2':{'usr_name':'zmy', 'score':257,'usr_pic_idx':4}

                    })
def get_usr_arch(usr_id):
    return [
            {'arch_id': 111, 'arch_score': 5},
            {'arch_id': 222, 'arch_score': 15},
            {'arch_id': '3sda', 'arch_score': 25},
            {'arch_id': 'sd', 'arch_score': 35},
            {'arch_id': '12', 'arch_score': 15},
            {'arch_id': 'wqw', 'arch_score': 115},
            {'arch_id': '121', 'arch_score': 35}
        ]

def rank(request):
    if request.method == 'POST':
        if 'usr_id' in request.POST:
            usr_id = request.POST['usr_id']
            usr_dict_info = json.loads(get_all_usr_info())
            list_all_rank = {}
            for key in usr_dict_info.keys():
                list_all_rank[key] = usr_dict_info[key]['score']
            sorted_rank =  sorted(list_all_rank.items(), key=lambda list_all_rank: list_all_rank[1])
            sorted_rank.reverse()
            if len(sorted_rank) > 10:
                sorted_rank = sorted_rank[0:10]
            response = []
            for usr_id, usr_score in sorted_rank:
                unit_dict = {}
                unit_dict['usr_id'] = usr_id
                unit_dict['score'] = usr_score
                unit_dict['usr_pic_idx'] = usr_dict_info[usr_id]['usr_pic_idx']
                response.append(unit_dict)
            return HttpResponse(json.dumps({'response':response}))
        else:
            raise Http404()
    else:
        raise Http404()

def arch_rank(request):
    if request.method == 'POST':
        if 'usr_id' in request.POST:
            usr_id = request.POST['usr_id']
            response = get_usr_arch(usr_id)
            return HttpResponse(json.dumps({'response' : response}))
        else:
            raise Http404()
    else:
        raise Http404()
