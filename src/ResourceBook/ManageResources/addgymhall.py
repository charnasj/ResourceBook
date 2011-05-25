from django.views.generic.list_detail import object_list
from django.views.generic.list_detail import object_detail
from django.views.generic.create_update import create_object
from django.views.generic.create_update import update_object
from django.views.generic.create_update import delete_object
from django.core.urlresolvers import reverse
 
from models import *
from django.http import HttpRequest, HttpResponse
from django.shortcuts import render_to_response
import userRegistration


def Add_resource_gymall_save(request):
    if 'client_id' in request.GET and request.GET['client_id']:
    	client_id= request.GET['client_id']
    	client_id= User.objects.get(pk=client_id)
    if 'Localgorvernment_ID' in request.GET and request.GET['Localgorvernment_ID']:
    	Localgorvernment_ID= request.GET['Localgorvernment_ID']
    	Localgorvernment_ID= LocalGovernment.objects.get(name=Localgorvernment_ID)
    if 'name' in request.GET and request.GET['name']:
    	name= request.GET['name']
    if 'description' in request.GET and request.GET['description']:
    	description= request.GET['description']
    if 'unit_price' in request.GET and request.GET['unit_price']:
        unit_price= request.GET['unit_price']
    if 'address' in request.GET and request.GET['address']:
        address= request.GET['address']
    if 'startdate' in request.GET and request.GET['startdate']:
        startdate= request.GET['startdate']
    if 'finishdate' in request.GET and request.GET['finishdate']:
        finishdate= request.GET['finishdate']
    vat = VAT.objects.get(name='basic')
    add_gymHall = RentResource(name=name, description=description,unit_price= unit_price, local_government_id = Localgorvernment_ID,vat_id = vat, address=address)
    #add_gymHall_dates = RentReservation(start=startdate, finish=finishdate,rent_resource_id=1,customer_id=1,order_item_id=1)
        

    add_gymHall.save()
    #add_gymHall_address.save()
    #add_gymHall_dates.save()
    
    return HttpResponse("Gym Hall added")

    
def Add_resource_gymall_form(request):
    return render_to_response('ManageResources/add_resource_gymhall.html')
