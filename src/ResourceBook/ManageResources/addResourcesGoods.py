from django.views.generic.list_detail import object_list
from django.views.generic.list_detail import object_detail
from django.views.generic.create_update import create_object
from django.views.generic.create_update import update_object
from django.views.generic.create_update import delete_object
from django.core.urlresolvers import reverse
 
from models import *
from django.http import HttpRequest, HttpResponse, HttpResponseNotFound
from django.shortcuts import render_to_response
from django.template import RequestContext



def Add_resources_goods_form(request):
    return render_to_response('ManageResources/add_resources_goods.html',context_instance=RequestContext(request))

def index(request):
    return render_to_response('ManageResources/index.html',context_instance=RequestContext(request))


def Add_resources_goods_save(request):
    if 'name' in request.GET and request.GET['name']:
        Name= request.GET['name']
    if 'description' in request.GET and request.GET['description']:
        desc= request.GET['description']
    if 'unit_price' in request.GET and request.GET['unit_price']:
        unitPrice = request.GET['unit_price']
    if 'local_government_id' in request.GET and request.GET['local_government_id']:
        localGovernmentId = request.GET['local_government_id']

        if not LocalGovernment.objects.filter(pk = localGovernmentId).exists():
            return render_to_response('ManageResources/Missing_ID.html',context_instance=RequestContext(request))
        
        localGovernmentId = LocalGovernment.objects.get(pk = localGovernmentId)
    if 'vat_id' in request.GET and request.GET['vat_id']:
        vatId = request.GET['vat_id']
        
        if not VAT.objects.filter(pk = vatId).exists():
            return render_to_response('ManageResources/Missing_ID.html',context_instance=RequestContext(request))
        
        vatId = VAT.objects.get(pk=vatId)
    if 'quantity' in request.GET and request.GET['quantity']:
        quantity = request.GET['quantity']
    if 'unit_type' in request.GET and request.GET['unit_type']:
        unitType = request.GET['unit_type']   
    add_resources = GoodsResource(name = Name, description = desc, unit_price = unitPrice, local_government_id = localGovernmentId, vat_id = vatId,
                             remaining_quantity = quantity, unit_type = unitType)
    add_resources.save()
    
    return render_to_response('ManageResources/add_resources_goods_added.html',context_instance=RequestContext(request))

