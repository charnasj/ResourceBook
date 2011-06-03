from django.views.generic.list_detail import object_list
from django.views.generic.list_detail import object_detail
from django.views.generic.create_update import create_object
from django.views.generic.create_update import update_object
from django.views.generic.create_update import delete_object
from django.core.urlresolvers import reverse
 
from django.http import HttpRequest, HttpResponse, HttpResponseNotFound
from django.shortcuts import render_to_response
from ResourceBook.ManageResources.models import Customer
from ResourceBook.ManageResources.models import Order
from ResourceBook.ManageResources.models import ResourceBookUser
from ResourceBook.ManageResources.models import GoodsResource
from ResourceBook.ManageResources.models import Resource
from ResourceBook.ManageResources.models import OrderItem
from django.contrib.auth.models import User

def View_Profile(request):
    if 'id_profile' in request.GET and request.GET['id_profile']:
        get_id = request.GET['id_profile']
    print("ID : " + get_id)
    
    
    if not Customer.objects.filter(pk = get_id).exists():
        return HttpResponseNotFound('<h1>Bad user id</h1>')
    
    queryset_customer = Customer.objects.get(pk = get_id)
    queryset_user = User.objects.get( pk = queryset_customer.user_id )
    
    queryset_order = Order.objects.all()#get(customer_id = queryset_customer.id)
    queryset_order_item = OrderItem.objects.all()
    
        
    dict = {'order':queryset_order, 'user':queryset_user, 'customer':queryset_customer , 'order_item':queryset_order_item}
    return render_to_response('ManageResources/view_profile.html' , {'data':dict}, context_instance=RequestContext(request))
    
def index(request):
    return render_to_response('ManageResources/index.html', context_instance=RequestContext(request))