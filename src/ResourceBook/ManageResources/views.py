from django.views.generic.list_detail import object_list
from django.views.generic.list_detail import object_detail
from django.views.generic.create_update import create_object
from django.views.generic.create_update import update_object
from django.views.generic.create_update import delete_object
from django.core.urlresolvers import reverse
 
from models import *
from django.http import HttpRequest, HttpResponse
from django.shortcuts import render_to_response

def LocalGovernment_list(request):
    """Show all notes"""
 
    return object_list(request, 
        queryset=LocalGovernment.objects.all(),
        template_name='ManageResources/list.html',
        template_object_name='LocalGovernment'
    )
    
def LocalGovernment_detail(request, id):
    
    return object_detail(request,
        queryset=LocalGovernment.objects.all(),
        object_id=id,
        template_name='ManageResources/detail.html',
        template_object_name='LocalGovernment'
    )

    
def Order_list(request):
    
    return object_list(request, queryset=Resource.objects.all(), template_name='ManageResources/orderDetail.html', template_object_name='LocalGovernment'
                       )

def index(request):
    return render_to_response('ManageResources/index.html')

def Add_resources_goods_form(request):
    return render_to_response('ManageResources/add_resources_goods.html')

