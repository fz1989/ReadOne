# Create your views here.
#!/usr/bin/env bash
from django.http import HttpResponse, Http404
import json

user_list = ["a","b","c","d"]
def get_all_usr_info():
    return json.dumps({
        'fz':{'usr_id': 'fz', 'score': 3600,'arch': 'sdsd','usr_pic_idx': 1},
        'dc':{'usr_id': 'dc', 'score': 3600,'arch': 'sdsd','usr_pic_idx': 1},
                      })

def get_all_friends(usr_id):
    return [
            {'usr_pic_idx': 1, 'usr_id': 'di ren jie'},
            {'usr_pic_idx': 2, 'usr_id': 'jie ren di'},
            {'usr_pic_idx': 3, 'usr_id': 'di jie ren'},
            {'usr_pic_idx': 4, 'usr_id': 'jie di ren'},
            {'usr_pic_idx': 5, 'usr_id': 'ren di jie'},
            {'usr_pic_idx': 6, 'usr_id': 'ren jie di'}
            ]

def get_usr_info(usr_id):
    return {'usr_id': 'fz', 'usr_pic_idx': 1}

def update_follow_friends(usr_id, friends_id):
    pass

def follow_friends(request):
    if request.method == 'POST':
        if 'usr_id' in request.POST and 'friends_id' in request.POST:
            usr_id = request.POST['usr_id']
            friends_id = request.POST['friends_id']
            update_follow_friends(usr_id, friends_id)
            return HttpResponse('YES')
        else:
            raise Http404()
    else:
        raise Http404()



def search_friends(request):
    response = None
    if request.method == 'POST':
        if 'usr_id' in request.POST:
            usr_id = request.POST['usr_id']
            response = get_usr_info(usr_id)
            return HttpResponse(json.dumps(response))
        else:
            raise Http404()
    else:
        raise Http404()


def show_friends(request):
    if request.method == 'POST':
        if 'usr_id' in request.POST:
            usr_id = request.POST['usr_id']
            response = get_all_friends(usr_id)
            return HttpResponse(json.dumps({'response': response}))
        else:
            raise Http404()
    else:
        raise Http404()
