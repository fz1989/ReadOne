#! /usr/bin/env python
#coding=utf-8
from django.http import HttpResponse
from django.http import Http404
import json
from random import randint

waiting_list = []
ready_list = []
competition_dict = {}
tot_dict = {}
cate_vector = []
def search_usr_info(usr_id):
    return {'usr_name':'fz','items':[1,2,3]}

def get_problem_by_cate(cate_id):
    return [{'prob_id': 1, 'text':u'狄仁杰', 'question':{'a':1,'b':2,'c':3}, 'answer':'a'},
            {'prob_id': 2, 'text':u'丧尸', 'question':{'a':2,'b':2,'c':4}, 'answer':'b'}]

def get_problem_by_item(item_id):
    if item_id == 1:
        return [{'prob_id': 3, 'text':u'测试', 'question':{'a':1,'b':2,'c':3}, 'answer':'a'},
            {'prob_id': 4, 'text':u'样例', 'question':{'a':2,'b':2,'c':4}, 'answer':'b'}]
    elif item_id == 2:
        return [{'prob_id': 5, 'text':u'玩一玩', 'question':{'a':1,'b':2,'c':3}, 'answer':'c'},
            {'prob_id': 6, 'text':u'不高兴', 'question':{'a':2,'b':2,'c':4}, 'answer':'c'}]
    else:
        return [{'prob_id': 7, 'text':u'科比布来恩特', 'question':{'a':1,'b':2,'c':3}, 'answer':'b'},
            {'prob_id': 8, 'text':u'篮球', 'question':{'a':2,'b':2,'c':4}, 'answer':'a'}]


def fetch_problem(creater):
    if tot_dict[creater] == 0:
        return None
    other_usr = competition_dict[creater]
    other_usr_item = search_usr_info(other_usr)['item']
    creater_usr_item = search_usr_info(creater)['item']

    common_item = list(set(creater_usr_item).intersection(set(other_usr_item)))

    problems = []
    for items in common_item:
        problems.append(get_problem_by_item(items))
        if len(problems) > 10:
            problems = problems[0: 10]
            return problems

    if len(problems) < 10:
        for cate_id in cate_vector:
            problems.append(get_problem_by_cate(cate_id))
            if len(problems) > 10:
                problems = problems[0: 10]
                return problems[0:10]
    tot_dict[creater] -= 1
    if tot_dict[creater] == 0:
        competition_dict.pop(creater)


    return problems



def update_usr_score(usr_id, score):
    return None

def find_follow(usr_a, usr_b):
    return True

def create_competition(request):
    response = None
    if request.method == 'POST':
        if 'usr_id' in request.POST:
            creater = request.POST['usr_id']
            if creater in waiting_list:
                response = {'response':'NOT READY'}
            elif creater in ready_list:
                prob_list = fetch_problem(creater)
                response = {'response':'OK', 'data': prob_list}
                ready_list.remove(creater)
            else:
                waiting_list.append(creater)
                response = {'response':'NOT READY'}
            return HttpResponse(json.dumps(response))
    else:
        raise Http404()

def join_competition(request):
    response = None
    if request.method == 'POST':
        if 'usr_id' in request.POST and 'creater_id' in request.POST:
            usr_id = request.POST['usr_id']
            creater_id = request.POST['creater_id']
            competition_dict[creater_id] = usr_id
            tot_dict[creater_id] = 2
            waiting_list.remove(creater_id)
            response = fetch_problem(creater_id)
            return HttpResponse(json.dumps({'response':'OK', 'data':response}))
    else:
        raise Http404()

def update_score(request):
    response = None
    if request.method == 'POST':
        if 'usr_id' in request.POST and 'add_score' in request.POST:
            usr_id = request.POST['usr_id']
            add_score = request.POST['add_score']
            update_usr_score(usr_id, add_score)
            response = "Successfully"
        return HttpResponse(response)
    else:
        raise Http404()

def show_competition(request):
    response = []
    if request.method == 'POST':
        if 'usr_id' in request.POST:
            usr_id = request.POST['usr_id']
            for other_usr in waiting_list:
                if find_follow(other_usr, usr_id) and find_follow(usr_id. other_usr):
                    response.append(other_usr)
        return HttpResponse(response)
    else:
        raise Http404()

def self_test(request):
    response = []
    if request.method == 'POST' and 'usr_id' in request.POST:
        usr_id = request.POST['usr_id']
        usr_info = search_usr_info(usr_id)
        usr_item = usr_info['items']
        for item_id in usr_item:
            problem = get_problem_by_item(item_id)
            response.extend(problem)
        idx = randint(0, len(problem) - 1)
        return HttpResponse(json.dumps(response[idx]))

