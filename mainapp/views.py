# -*- coding: utf-8 -*-

from django.http import JsonResponse
# from .serializers import PlayerSerializer
from django.views.decorators.csrf import csrf_exempt
from .models import *
from django.shortcuts import render
from django.core import serializers
import datetime
from django.core.files.storage import default_storage


######################################## 11-04-2020 #####################################################

def relay_items(request):
    all_relay_items = RelayGroup.objects.all().order_by('pk')    
    context={"all_relay_items":all_relay_items}
    return render(request, "templates/relay_items.html",context)

def ajax_update_relay_status (request):
    status = request.GET.get('status')
    relay_number = request.GET.get('relay_number')
    #import pdb;pdb.set_trace()
    try :
        relay = RelayGroup.objects.get(pk=relay_number)
        relay.r_status = True if status=="1" else False
        relay.r_lastupdateinfo = datetime.datetime.now()
        relay.save()
        data = {"Status": "Ok"}
    except :
        data = {"Status": "Error"}
    #print(data)
    return JsonResponse(data, safe=False)

def get_relay_group_status (request):
    #import pdb;pdb.set_trace()
    try :
        relay_group = list(RelayGroup.objects.all().values())
    except :
        relay_group = None
    #print(data)
    return JsonResponse(relay_group, safe=False)

