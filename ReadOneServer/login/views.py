# Create your views here.
#!/usr/bin/env bash
from django.http import HttpResponse

def login(request):
    return HttpResponse("login")
