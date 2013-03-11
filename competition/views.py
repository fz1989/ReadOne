from django.http import HttpResponse
from django.http import Http404
import json

waiting_list = []
ready_list = []
competition_dict = {}
tot_dict = {}
cate_vector = []
def search_usr_info(usr_id):
    pass

def get_problem_by_cate(cate_id):
    pass

def get_problem_by_item(item_id):
    pass

def fetch_problem(creater):
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
                response = "NOT READY"
            elif creater in ready_list:
                response = fetch_problem(creater)
                ready_list.remove(creater)
            else:
                waiting_list.append(creater)
                response = "NOT READY"
            return HttpResponse(response)
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
            response = fetch_problem(creater_id)
            return HttpResponse(response)
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

