# Create your views here.
#!/usr/bin/env bash
from django.http import HttpResponse
import json

def get_all_category():
    return json.dumps({'resopnse':[ {'cate_id':'123', 'cate_name':'snake'},
                        {'cate_id':'234', 'cate_name':'dragon'}]})

def search_cate_items(cate_id):
    return json.dumps([ {'item_id':cate_id, 'abstract':'nimeide', 'title':'QNMLGBD'},
                        {'item_id':1234, 'abstract':'nimeide', 'title':'QNMLGBD'}])

def items(request, usr_id):
    return HttpResponse("items")

def cate(request):
    response = get_all_category()
    return HttpResponse(response)

def subcate(request, cate_id):
    try:
        cate_id = int(cate_id)
    except ValueError:
        raise Http404()
    response = search_cate_items(cate_id)
    return HttpResponse(response)
