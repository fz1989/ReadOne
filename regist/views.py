# Create your views here.
#!/usr/bin/env bash
from django.http import HttpResponse, Http404

def regist_usr_account(usr_id, usr_pwd):
    return False


def check_usr_exist(usr_id):
    return False

def regist(request):
    if request.method == 'POST':
        if 'usr_id' in request.POST and 'usr_pwd' in request.POST:
            usr_id = request.POST['usr_id']
            usr_pwd = request.POST['usr_pwd']
            if check_usr_exist(usr_id):
                return HttpResponse("NO")
            else:
                regist_usr_account(usr_id, usr_pwd)
                return HttpResponse("YES")
        else:
            raise Http404()
    else:
        raise Http404()
