from django.views.generic.list_detail import object_list
from django.views.generic.list_detail import object_detail
from django.views.generic.create_update import create_object
from django.views.generic.create_update import update_object
from django.views.generic.create_update import delete_object
from django.core.urlresolvers import reverse
from django.http import HttpRequest, HttpResponse
from django.shortcuts import render_to_response

from models import *

def placeGoodsOrder(request):
    return HttpResponse("A new Order has been saved!")

def Place_order_goods_form(request):
    return render_to_response('ManageResources/place_goods_order_form.html')

def Place_order_goods_save(request):
    return render_to_response('ManageResources/place_goods_order_save.html')
