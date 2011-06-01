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

#def LocalGovernment_list(request):
#    """Show all notes"""
# 
#    return object_list(request, 
#        queryset=LocalGovernment.objects.all(),
#        template_name='ManageResources/list.html',
#        template_object_name='LocalGovernment'
#    )
#    
#def LocalGovernment_detail(request, id, message):
#    
#    return object_detail(request,
#        queryset=LocalGovernment.objects.all(),
#        object_id=id,
#        object_message=message,
#        template_name='ManageResources/detail.html',
#        template_object_name='LocalGovernment'
#    )
#

def View_available_goods(request):
    for goods in GoodsResource.objects.all():
        print(goods.id)
#    return object_list(request, 
#        queryset=GoodsResource.objects.all(),
#        template_name='ManageResources/view_available_goods.html',
#        template_object_name='GoodsResource'
#        )
        queryset=GoodsResource.objects.all()
        return render_to_response('ManageResources/view_available_goods.html' , {'goods':queryset})

    
def View_available_goods_detail(request, id):
    
    return object_detail(request,
        queryset=GoodsResource.objects.all(),
        object_id=id,
        template_name='ViewAvailableGoods/detail.html',
        template_object_name='ViewAvailableGoods'
    )
