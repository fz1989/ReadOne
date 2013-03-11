# Create your views here.
#!/usr/bin/env bash
from django.http import HttpResponse, Http404
import json
def get_all_usr_info():
    return json.dumps({
                        'fz':{'usr_name':'fz', 'score':256},
                        'dc':{'usr_name':'dc', 'score':250},
                        'wl':{'usr_name':'wl', 'score':253},
                        'zmy':{'usr_name':'zmy', 'score':255}
                    })

def rank(request):
    if request.method == 'POST':
        if 'usr_id' in request.POST:
            usr_id = request.POST['usr_id']
            usr_dict_info = get_all_usr_info()
            list_all_rank = {}
            for key in usr_dict_info.keys():
                list_all_rank[key] = usr_dict_info[key]['score']
            sorted_rank =  sorted(list_all_rank.items(), key=lambda list_all_rank: list_all_rank[1])
            sorted_rank.reverse()
            if len(sorted_rank) > 10:
                sorted_rank = sorted_rank[0:10]
            response = {}
            for usr_id, usr_score in sorted_rank:
                response[usr_id] = usr_score
            return HttpResponse(json.dumps(response))
        else:
            raise Http404()
    else:
        raise Http404()
