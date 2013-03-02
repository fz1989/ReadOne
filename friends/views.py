# Create your views here.
#!/usr/bin/env bash
from django.http import HttpResponse
import json

user_list = ["a","b","c","d"]
def get_all_usr_info():
    return json.dumps([ {'userid':'di ren jie', 'score':'3600','achienemwnt':'ji bai bike damo wang','picture':'hello python'},
                        {'userid':'cao sang shi', 'score':'3600','achienemwnt':'ji bai bike damo wang','picture':'hello python'}
                    ])

def search_usr_info(usr_id):
    return json.dumps({'username':123,
                        'score':'3600',
                        'achienemwnt':'ji bai bike damo wang',
                        'picture':'hello python'})

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
    if request.method == 'GET':
        if 'action' in request.GET:
            action = request.GET['action']
            if (action == 'search'):
                usr_id = request.GET['usr_id']
                response = HttpResponse(search_friends(usr_id))
            else:
                usr_id = request.GET['usr_id']
                friends_id = request.GET['friends_id']
                response = HttpResponse(follow_friends(usr_id, friends_id))
    return HttpResponse(response)
