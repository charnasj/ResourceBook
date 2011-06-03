from django.views.generic.list_detail import object_list
from django.views.generic.list_detail import object_detail
from django.views.generic.create_update import create_object
from django.views.generic.create_update import update_object
from django.views.generic.create_update import delete_object
from django.core.urlresolvers import reverse
from django.http import HttpRequest, HttpResponse
from django.shortcuts import render_to_response
from models import *
import datetime

def placeGoodsOrder(request):
    return HttpResponse("A new Order has been saved!")

def Place_order_goods_save(request):
    #Creating the new Order according to the ressources
    if 'id' in request.GET and request.GET['id']:
        resourceId= request.GET['id']
    if 'quantity' in request.GET and request.GET['quantity']:
        quantity= request.GET['quantity']
    #1. get the target resource
    resource    = Resource.objects.get(id=resourceId)
    print resource.name
    #2. create the invoice
    invoice     = Invoice(invoiceDate = datetime.datetime.now())
    invoice.save()
    
    #3. create the order
    order       = Order(order_date = datetime.datetime.now(), status = 'new', customer_id = session.get('customer_id'), invoice_id = invoice.id)
    order.save();
    
    #4. create invoice lines
    invoiceLine = InvoiceLine(name = resource.name, description = resource.description, dueDate = datetime.datetime.now(), units = quantity, amount = resource.price, vat_id = resource.vat_id, )
    invoiceLine.save()
    
    #5. create order item
    orderItem   = OrderItem(order_id = order.id,resource_id = resource.id,invoice_line_id = invoiceLine.id)
    orderItem.save()
    
    return HttpResponse("Order Saved")
    
