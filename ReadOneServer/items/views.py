# Create your views here.
#!/usr/bin/env bash
from django.http import HttpResponse

def items(request):
    return HttpResponse("items")
