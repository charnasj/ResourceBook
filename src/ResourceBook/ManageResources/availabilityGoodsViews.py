from django.views.generic.list_detail import object_list
from django.views.generic.list_detail import object_detail
from django.views.generic.create_update import create_object
from django.views.generic.create_update import update_object
from django.views.generic.create_update import delete_object
from django.core.urlresolvers import reverse
 
from django.http import HttpRequest, HttpResponse
from django.shortcuts import render_to_response
from ResourceBook.ManageResources.models import GoodsResource
from ResourceBook.ManageResources.models import Resource

def View_available_goods(request):
    queryset=GoodsResource.objects.all()
    return render_to_response('ManageResources/view_available_goods.html' , {'goods':queryset})

    
def index(request):
    return render_to_response('ManageResources/index.html')