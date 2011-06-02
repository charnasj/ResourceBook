import ResourceBook.ManageResources.models
from django.views.generic.list_detail import object_list
from django.views.generic.list_detail import object_detail
from django.shortcuts import render_to_response
from ResourceBook.ManageResources.models import GoodsResource
<<<<<<< HEAD
=======
from ResourceBook.ManageResources.models import Resource
>>>>>>> origin/master

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
<<<<<<< HEAD
    goods = GoodsResource.objects.get(pk=1)
    print('TEST')
    print(goods.name)
    for goods in GoodsResource.objects.all():
        print(goods.name)

    return object_list(request,
                        queryset=GoodsResource.objects.all(),
                        template_name='ViewAvailableGoods/view_available_goods.html',
                        template_object_name='GoodsResource')  


def View_available_goods_detail(request, id):  
=======
    for goods in GoodsResource.objects.all():
        print(goods.name)
    return object_list(request, 
        queryset=GoodsResource.objects.all(),
        template_name='ViewAvailableGoods/view_available_goods.html',
        template_object_name='ResourceBook.ManageResources.models.GoodsResource'
    )  
    
def View_available_goods_detail(request, id):
    
>>>>>>> origin/master
    return object_detail(request,
        queryset=GoodsResource.objects.all(),
        object_id=id,
        template_name='ViewAvailableGoods/detail.html',
<<<<<<< HEAD
        template_object_name='GoodsResource'
=======
        template_object_name='ViewAvailableGoods'
>>>>>>> origin/master
    )
