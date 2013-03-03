# Create your views here.
#!/usr/bin/env bash
from django.http import HttpResponse
import json
import recommond

def get_all_category():
    return json.dumps({'resopnse':[ {'cate_id':'123', 'cate_name':'snake'},
                        {'cate_id':'234', 'cate_name':'dragon'}]})

def search_cate_items(cate_id):
    return json.dumps([ {'item_id':cate_id, 'abstract':'nimeide', 'title':'QNMLGBD'},
                        {'item_id':1234, 'abstract':'nimeide', 'title':'QNMLGBD'}])

def items(request):
    resopnse = None
    if request.method == 'POST':
        if 'usr_id' in request.POST and 'item_id' in request.POST:
            usr_id = request.POST['usr_id']
            item_id = request.POST['item_id']
            response = get_item_info(item_id)
            cate_id = get_item_cate(item_id)
            update_usr_behavior(usr_id, cate_id, 1)
        else:
            raise Http404()
    else:
        raise Http404()
    return HttpResponse(response)

def recommond_items(request):
    response = None
    if request.method == 'POST' and 'usr_id' in request.POST:
        usr_id = request.POST['usr_id']
        response = get_recommond_items(usr_id)
    return HttpResponse(response)


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
