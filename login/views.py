#! /usr/bin/env python
#coding=utf-8
from django.http import HttpResponse,Http404

def check_usr_pwd(usr_name, usr_pwd):
    return True


def login(request):
    if request.method == 'POST':
        if 'usr_id' in request.POST and 'usr_pwd' in request.POST:
            usr_id = request.POST['usr_id']
            usr_pwd = request.POST['usr_pwd']
            if check_usr_pwd(usr_id, usr_pwd):
                return HttpResponse("YES")
            else:
                return HttpResponse("NO")
        else:
            raise Http404()
    else:
        raise Http404()
