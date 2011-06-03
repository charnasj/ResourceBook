from django.views.generic.list_detail import object_list
from django.views.generic.list_detail import object_detail
from django.views.generic.create_update import create_object
from django.views.generic.create_update import update_object
from django.views.generic.create_update import delete_object
from django.core.urlresolvers import reverse
from django.http import HttpRequest, HttpResponse
from django.shortcuts import render_to_response
from models import *
from django.template import RequestContext
import datetime

def placeGoodsOrder(request):
    return HttpResponse("A new Order has been saved!")

def Place_order_goods_form(request):
    return render_to_response('ManageResources/place_goods_order_form.html')

def Place_order_goods_save(request):
    quantity = 0
    #Creating the new Order according to the ressources
    if 'id' in request.GET and request.GET['id']:
        resourceId= request.GET['id']
    if 'quantity' in request.GET and request.GET['quantity']:
        quantity= request.GET['quantity']
    
    #0. get the current customer
    customer    = Customer.objects.get(id=request.session.get('customer_id'))
    #1. get the target resource
    resource    = Resource.objects.get(id=resourceId)
    #2. create the invoice
    invoice     = Invoice(invoiceDate = datetime.datetime.now())
    invoice.save()
    
    #3. create the order
    order       = Order(order_date = datetime.datetime.now(), status = 'new', customer_id = customer, invoice_id = invoice)
    order.save();
    
    #4. create invoice lines
    invoiceLine = InvoiceLine(name = resource.name, description = resource.description, dueDate = datetime.datetime.now(), units = quantity, amount = resource.unit_price, vat_id = resource.vat_id, )
    invoiceLine.save()
    
    #5. create order item
    orderItem   = OrderItem(order_id = order,resource_id = resource)        #TODO add ,invoice_line_id = invoiceLine.id)
    orderItem.save()
    
    #6. update invoice total
    invoice.total       = invoiceLine.total
    invoice.totalExcl   = invoiceLine.totalExcl
    invoice.totalIncl   = invoiceLine.totalIncl
    invoice.totalVat    = invoiceLine.totalIncl - invoiceLine.totalExcl
    invoice.round       = 0
    invoice.save()
    
    #now will return the paypayl url
    pp = paypal.PayPal()
    token = pp.SetExpressCheckout(invoice.totalIncl)
    paypal_url = pp.PAYPAL_URL + token
    payload = {'paypal_url':paypal_url}
    
    return HttpResponse('paypal_order.html', payload, RequestContext(request))
    
