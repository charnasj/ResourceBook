from django.views.generic.list_detail import object_list
from django.views.generic.list_detail import object_detail
from django.views.generic.create_update import create_object
from django.views.generic.create_update import update_object
from django.views.generic.create_update import delete_object
from django.core.urlresolvers import reverse
 
from django.http import HttpRequest, HttpResponse
from django.shortcuts import render_to_response
from ResourceBook.ManageResources.models import Customer
from ResourceBook.ManageResources.models import Order
from ResourceBook.ManageResources.models import ResourceBookUser
from django.contrib.auth.models import User

def View_Profile(request):
    print("<==============================================================>")
    if 'id_profile' in request.GET and request.GET['id_profile']:
        get_id = request.GET['id_profile']
    print("ID : " + get_id)
    
    queryset_customer = Customer.objects.get(pk=get_id)
    
    print(queryset_customer.shipping_address)
    
    
    queryset_user = User.objects.get( pk = queryset_customer.user_id )
    
    print(queryset_user.pk)
    print(queryset_user.username)
    
    queryset_order = Order.objects.get(customer_id = queryset_customer.id)

    #return render_to_response('ManageResources/view_profile.html' , {'customer':queryset_customer, 'user':queryset_user})
    return render_to_response('ManageResources/view_profile.html' , {'customer':queryset_customer, 'order':queryset_order, 'user':queryset_user})
    
def index(request):
    return render_to_response('ManageResources/index.html')