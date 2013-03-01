# Create your views here.
#!/usr/bin/env bash
from django.http import HttpResponse

def regist(request):
    return HttpResponse("regist")
