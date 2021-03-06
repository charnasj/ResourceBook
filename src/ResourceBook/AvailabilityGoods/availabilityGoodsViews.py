import ResourceBook.ManageResources.models
from django.views.generic.list_detail import object_list
from django.views.generic.list_detail import object_detail
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
        print(goods.name)
    return object_list(request, 
        queryset=GoodsResource.objects.all(),
        template_name='ViewAvailableGoods/view_available_goods.html',
        template_object_name='ResourceBook.ManageResources.models.GoodsResource',
        context_instance=RequestContext(request)
    )  
    
def View_available_goods_detail(request, id):  
    for goods in GoodsResource.objects.all():
        print(goods.name)
    return object_list(request, 
        queryset=GoodsResource.objects.all(),
        template_name='ViewAvailableGoods/view_available_goods.html',
        template_object_name='ResourceBook.ManageResources.models.GoodsResource',
        context_instance=RequestContext(request)
    )  
    
def View_available_goods_detail(request, id):
    return object_detail(request,
        queryset=GoodsResource.objects.all(),
        object_id=id,
        template_name='ViewAvailableGoods/detail.html',
        template_object_name='ViewAvailableGoods',
        context_instance=RequestContext(request)
    )
