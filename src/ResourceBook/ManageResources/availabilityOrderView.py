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
from ResourceBook.ManageResources.models import OrderItem
from ResourceBook.ManageResources.models import Order
from ResourceBook.ManageResources.models import Customer
from ResourceBook.ManageResources.models import GoodsOrderItem
from ResourceBook.ManageResources.models import RentsOrderItem
from django.template import RequestContext


def View_available_orders(request):
   
       
#    return object_list(request, 
#        queryset=GoodsResource.objects.all(),
#        template_name='ManageResources/view_available_goods.html',
#        template_object_name='GoodsResource'
#        )
        queryset=OrderItem.objects.all()
        return render_to_response('PlaceOrder/active_order.html' , {'orders':queryset}, context_instance=RequestContext(request))

    
def View_available_orders_detail(request, id):
    
    return object_detail(request,
        queryset=OrderItem.objects.all(),
        object_id=id,
        template_name='ViewAvailableGoods/detail.html',
        template_object_name='ViewAvailableOrders',
        context_instance=RequestContext(request)
    )
