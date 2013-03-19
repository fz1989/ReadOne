#! /usr/bin/env python
#coding=utf-8
from django.http import HttpResponse
from django.http import Http404
import json
from random import randint
from userCtl.models import *
from itemCtl.models import *

waiting_list = []
ready_list = []
competition_dict = {}
tot_dict = {}
cate_vector = []
def search_user_info(user_id):
    user_info = get_user(user_id)
    return {'user_name': user_info[0], 'items': user_info[4]}

def get_problem_by_cate(cate_id):
    ret = []
    item_list = get_cate(cate_id)[1]
    for item_id in item_list:
        prob_name_list = get_item(item_id)[4]
        for prob in prob_ame_list:
            prob_info = get_prob(item_id,prob)
            ret.append({'prob_id': prob_info[1], 'text': prob_info[1], 'question': prob_info[2],
                'answer': prob_info[3]})

    return ret

def get_problem_by_item(item_id):
    ret = []
    prob_name_list = get_item(item_id)[4]
    for prob in prob_ame_list:
        prob_info = get_prob(item_id,prob)
        ret.append({'prob_id': prob_info[1], 'text': prob_info[1], 'question': prob_info[2], 'answer': prob_info[3]})
    return ret


def fetch_problem(creater):
    if tot_dict[creater] == 0:
        return None
    other_user = competition_dict[creater]
    other_user_item = search_user_info(other_user)['item']
    creater_user_item = search_user_info(creater)['item']

    common_item = list(set(creater_user_item).intersection(set(other_user_item)))

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



def update_user_score(user_id, score):
    set_rank(user_id, get_rank(user_id) + score)


def find_follow(user_a, user_b):
    return get_follow(user_a, user_b)

def create_competition(request):
    response = None
    if request.method == 'POST':
        if 'user_id' in request.POST:
            creater = request.POST['user_id']
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
        if 'user_id' in request.POST and 'creater_id' in request.POST:
            user_id = request.POST['user_id']
            creater_id = request.POST['creater_id']
            competition_dict[creater_id] = user_id
            tot_dict[creater_id] = 2
            waiting_list.remove(creater_id)
            response = fetch_problem(creater_id)
            return HttpResponse(json.dumps({'response':'OK', 'data':response}))
    else:
        raise Http404()

def update_score(request):
    response = None
    if request.method == 'POST':
        if 'user_id' in request.POST and 'add_score' in request.POST:
            user_id = request.POST['user_id']
            add_score = request.POST['add_score']
            update_user_score(user_id, add_score)
            response = "Successfully"
        return HttpResponse(response)
    else:
        raise Http404()

def show_competition(request):
    response = []
    if request.method == 'POST':
        if 'user_id' in request.POST:
            user_id = request.POST['user_id']
            for other_user in waiting_list:
                if find_follow(other_user, user_id) and find_follow(user_id. other_user):
                    response.append(other_user)
        return HttpResponse(response)
    else:
        raise Http404()

def self_test(request):
    response = []
    if request.method == 'POST' and 'user_id' in request.POST:
        user_id = request.POST['user_id']
        user_info = search_user_info(user_id)
        user_item = user_info['items']
        for item_id in user_item:
            problem = get_problem_by_item(item_id)
            response.extend(problem)
        idx = randint(0, len(problem) - 1)
        return HttpResponse(json.dumps(response[idx]))

