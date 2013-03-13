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

def search_usr_info(usr_id):
    return json.dumps({'usr_id': 'fz', 'score': 3600,'arch': 'sdsd','usr_pic_idx': 1})

def update_follow_friends_relationship(usr_id, friends_id):
    '''
    two users will become friends if and noly if they follow each other
    '''
    if not update_follow(usr_id, friends_id):
        return None

    follow_find(friends_id, usr_id)
    add_friends(usr_id, friends_id)



def follow_friends(usr_id, friends_id):
    '''
    follow one user and update their follow's info between the two users
    '''
    if friens_id not in usr_list:
        return json.dumps({'Message':'Error: Friends Not Found'})
    else:
        if not update_follow_friends_relationship(usr_id, friends_id):
            return json.dumps({'Message':'Follow Failed!'})
        else:
            return json.dumps({'Message':'Follow Successfully!'})

def search_friends(usr_id):
    '''
    just search for one user
    '''
    if not usr_id:
        info = get_all_usr_info()
    else:
        info = search_usr_info(usr_id)
    return info

def friends(request):
    response = None
    if request.method == 'POST':
        if 'action' in request.POST:
            action = request.POST['action']
            if (action == 'search'):
                usr_id = request.POST['usr_id']
                response = HttpResponse(search_friends(usr_id))
            else:
                usr_id = request.POST['usr_id']
                friends_id = request.POST['friends_id']
                response = HttpResponse(follow_friends(usr_id, friends_id))
    return HttpResponse(response)


def show_friends(request):
    if request.method == 'POST':
        if 'usr_id' in request.POST:
            usr_id = request.POST['usr_id']
            response = get_all_friends(usr_id)
            return HttpResponse(json.dumps({'response':response}))
        else:
            raise Http404()
    else:
        raise Http404()
