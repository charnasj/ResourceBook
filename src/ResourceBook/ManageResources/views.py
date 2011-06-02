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
    queryset_rent=RentResource.objects.all()
    queryset_goods = GoodsResource.objects.all()
    return render_to_response('ManageResources/index.html', {'rent':queryset_rent , 'goods':queryset_goods})

def Goods_details(request, id):
    
    return object_detail(request,
        queryset=GoodsResource.objects.all(),
        object_id=id,
        template_name='ManageResources/detail_goods.html',
        template_object_name='GoodsResource'
    )
    
def Rent_details(request, id):
    
    return object_detail(request,
        queryset=RentResource.objects.all(),
        object_id=id,
        template_name='ManageResources/detail_rent.html',
        template_object_name='RentResource'
    )


def Add_resources_goods_form(request):
    return render_to_response('ManageResources/add_resources_goods.html')

def Add_resource_gymhall_form(request):
    return render_to_response('ManageResources/add_resource_gymhall.html')

def View_available_goods(request):
    return render_to_response('ManageResources/view_available_goods.html')

def View_Profile(request):
    return render_to_response('ManageResources/view_profile.html')

def View_available_gymhall(request):
    return render_to_response('ManageResources/view_available_gymhall.html')

