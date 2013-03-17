# Create your views here.
#! /usr/bin/env python
#coding=utf-8
from django.http import HttpResponse, Http404
from userCtl.models import *

def regist(request):
    if request.method == 'POST':
        if 'user_id' in request.POST and 'user_pwd' in request.POST:
            user_id = request.POST['user_id']
            user_pwd = request.POST['user_pwd']
            if not add_user(user_id, user_pwd):
                return HttpResponse("NO")
            else:
                return HttpResponse("YES")
        else:
            raise Http404()
    else:
        raise Http404()
