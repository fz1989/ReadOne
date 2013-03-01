# Create your views here.
#!/usr/bin/env bash
from django.http import HttpResponse

def rank(request):
    return HttpResponse("rank")
