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

def View_Profile(request):
    if 'id_profile' in request.GET and request.GET['id_profile']:
        id= request.GET['id_profile']
    queryset=Customer.objects.get(pk=id)
    queryset_order = Order.objects.get(customer_id = id)
    return render_to_response('ManageResources/view_profile.html' , {'user':queryset, 'order':queryset_order})

    
def index(request):
    return render_to_response('ManageResources/index.html')