from django.views.generic.list_detail import object_list
from django.views.generic.list_detail import object_detail
from django.views.generic.create_update import create_object
from django.views.generic.create_update import update_object
from django.views.generic.create_update import delete_object
from django.core.urlresolvers import reverse
 
from models import *
from django.http import HttpRequest, HttpResponse, HttpResponseNotFound
from django.shortcuts import render_to_response
#import userRegistration


def Add_resource_gymhall_save(request):
    if 'client_id' in request.GET and request.GET['client_id']:
    	client_id= request.GET['client_id']
    	client_id= ResourceBookUser.objects.get(pk=client_id)
    if 'Localgorvernment_ID' in request.GET and request.GET['Localgorvernment_ID']:
    	Localgorvernment_ID= request.GET['Localgorvernment_ID']
        
        if not LocalGovernment.objects.filter(pk = Localgorvernment_ID).exists():
            return HttpResponseNotFound('<h1><FONT COLOR="red" >Local Government ID doesn\'t exist</FONT></h1>', context_instance=RequestContext(request))
        
        Localgorvernment_ID= LocalGovernment.objects.get(pk=Localgorvernment_ID)        
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
    if 'vat_id' in request.GET and request.GET['vat_id']:
        vatId = request.GET['vat_id']
        
        if not VAT.objects.filter(pk = vatId).exists():
            return HttpResponseNotFound('<h1><FONT COLOR="red" >VAT ID doesn\'t exist</FONT></h1>', context_instance=RequestContext(request))
        
        vat = VAT.objects.get(pk=vatId)
    add_gymHall = RentResource(name=name, description=description,unit_price= unit_price, local_government_id = Localgorvernment_ID,vat_id = vat, address=address)
    #add_gymHall_dates = RentReservation(start=startdate, finish=finishdate,rent_resource_id=1,customer_id=1,order_item_id=1)
        

    add_gymHall.save()
    #add_gymHall_address.save()
    #add_gymHall_dates.save()
    
    return render_to_response('ManageResources/add_resource_gymhall_added.html', context_instance=RequestContext(request))

    
def Add_resource_gymhall_form(request):
    return render_to_response('ManageResources/add_resource_gymhall.html', context_instance=RequestContext(request))

def index(request):
    return render_to_response('ManageResources/index.html', context_instance=RequestContext(request))
