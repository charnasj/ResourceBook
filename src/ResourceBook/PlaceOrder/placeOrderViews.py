from django.views.generic.list_detail import object_list
from django.views.generic.list_detail import object_detail
from django.views.generic.create_update import create_object
from django.views.generic.create_update import update_object
from django.views.generic.create_update import delete_object
from django.core.urlresolvers import reverse
 
from django.http import HttpRequest, HttpResponse
from django.shortcuts import render_to_response
from ResourceBook.ManageResources.models import LocalGovernment

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
#    
#def Order_list(request):
#    
#    return object_list(request, queryset=Resource.objects.all(), template_name='ManageResources/orderDetail.html', template_object_name='LocalGovernment'
#)
#
#def index(request):
#    return HttpResponse("This is an eGovernment platform for resource management.")
#
#
#def Add_resource_gymall_save(request):
#    if 'name' in request.GET and request.GET['name']:
#        name= request.GET['name']
#    if 'description' in request.GET and request.GET['description']:
#        description= request.GET['description']
#    if 'unit_price' in request.GET and request.GET['unit_price']:
#        unit_price= request.GET['unit_price']
#    if 'address' in request.GET and request.GET['address']:
#        address= request.GET['address']
#    if 'startdate' in request.GET and request.GET['startdate']:
#        startdate= request.GET['startdate']
#    if 'finishdate' in request.GET and request.GET['finishdate']:
#        finishdate= request.GET['finishdate']
#   # add_gymHall = Resource(name=name, description=description,local_government_id = 1,vat_id = 1)
#   # add_gymHall_address = RentResource(address=address)
#   # add_gymHall_dates = RentReservation(start=startdate, finish=finishdate,rent_resource_id=1,customer_id=1,order_item_id=1)
#        
#
#    #add_gymHall.save()
#    #add_gymHall_address.save()
#    #add_gymHall_dates.save()
#    
#    return HttpResponse("Gym Hall added")

    
def Place_order(request):
    return render_to_response('PlaceOrder/place_order.html', context_instance=RequestContext(request))
