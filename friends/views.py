# Create your views here.
#!/usr/bin/env bash
from django.http import HttpResponse

def friends(request):
    return HttpResponse("friends")
