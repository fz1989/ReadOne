#! /user/bin/env python
#coding=utf-8
from django.http import HttpResponse,Http404
from userCtl.models import *

def check_user_pwd(user_name, user_pwd):
    return user_pwd == get_pwd(user_name)


def login(request):
    if request.method == 'POST':
        if 'user_id' in request.POST and 'user_pwd' in request.POST:
            user_id = request.POST['user_id']
            user_pwd = request.POST['user_pwd']
            if check_user_pwd(user_id, user_pwd):
                return HttpResponse("YES")
            else:
                return HttpResponse("NO")
        else:
            raise Http404()
    else:
        raise Http404()
