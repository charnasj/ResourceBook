from django.views.generic.list_detail import object_list
from django.views.generic.list_detail import object_detail
from django.views.generic.create_update import create_object
from django.views.generic.create_update import update_object
from django.views.generic.create_update import delete_object
from django.core.urlresolvers import reverse
 
from models import *
from django.http import HttpRequest, HttpResponse
from django.shortcuts import render_to_response
from django.template import RequestContext


def LocalGovernment_list(request):
    """Show all notes"""
 
    return object_list(request, 
        queryset=LocalGovernment.objects.all(),
        template_name='ManageResources/list.html',
        template_object_name='LocalGovernment'
    )
    
def LocalGovernment_detail(request, id):
    
    return object_detail(request,
        queryset=LocalGovernment.objects.all(),
        object_id=id,
        template_name='ManageResources/detail.html',
        template_object_name='LocalGovernment'
    )

    
def Order_list(request):
    return object_list(request, queryset=Resource.objects.all(), template_name='ManageResources/orderDetail.html', template_object_name='LocalGovernment')

def index(request):
    queryset_rent=RentResource.objects.all()
    queryset_goods = GoodsResource.objects.all()
    return render_to_response('ManageResources/index.html', {'rent':queryset_rent , 'goods':queryset_goods}, context_instance=RequestContext(request))

def Goods_details(request, id):
    
    return object_detail(request,
        queryset=GoodsResource.objects.all(),
        object_id=id,
        template_name='ManageResources/detail_goods.html',
        template_object_name='GoodsResource'
    )
    
def Rent_details(request, id):
    
    return object_detail(request,
        queryset=RentResource.objects.all(),
        object_id=id,
        template_name='ManageResources/detail_rent.html',
        template_object_name='gymResource'
    )

def Place_gym_order(request, id):
    
    quantity = 0
    #Creating the new Order according to the ressources
    if 'id' in request.GET and request.GET['id']:
        resourceId= request.GET['id']
    if 'quantity' in request.GET and request.GET['quantity']:
        quantity= request.GET['quantity']
    
    #0. get the current customer
#    customer    = Customer.objects.get(id=request.session.get('customer_id'))
    customer    = Customer.objects.get(id=1)
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
    if 'startDate' in request.GET and request.GET['startDate']:
        startDate= request.GET['startDate']
    #if the string input from the web page has to be converted into a date 
    #here is how it is done, the date should look like this "03/06/11"
#    start_date_as_date = datetime.datetime.strptime(startDate, "%d/%m/%y")
        
    if 'endDate' in request.GET and request.GET['endDate']:
        endDate= request.GET['endDate']
    #TODO add ,invoice_line_id = invoiceLine.id)
    new_RentsOrderItem = RentsOrderItem(name=customer.user.username, description = "Some description", 
                                        unit_price=resource.unit_price, order_id=order, resource_id=resource, start=startDate, finish=endDate)
    new_RentsOrderItem.save()
    #6. update invoice total
    invoice.total       = invoiceLine.total
    invoice.totalExcl   = invoiceLine.totalExcl
    invoice.totalIncl   = invoiceLine.totalIncl
    invoice.totalVat    = invoiceLine.totalIncl - invoiceLine.totalExcl
    invoice.round       = 0
    invoice.save()
    
    #now will return the paypayl url
#    pp              = PayPal()
#    token           = pp.SetExpressCheckout(invoice.totalIncl)
#    paypal_url      = pp.PAYPAL_URL + token
#    payload         = {'paypal_url':paypal_url}
#    
#    return HttpResponse('paypal_order.html', payload, RequestContext(request))
    return HttpResponse("Rent order created.")

def Add_resources_goods_form(request):
    return render_to_response('ManageResources/add_resources_goods.html', context_instance=RequestContext(request))

def Add_resource_gymhall_form(request):
    return render_to_response('ManageResources/add_resource_gymhall.html', context_instance=RequestContext(request))

def View_available_goods(request):
    return render_to_response('ManageResources/view_available_goods.html', context_instance=RequestContext(request))

def View_Profile(request):
    return render_to_response('ManageResources/view_profile.html', context_instance=RequestContext(request))

def View_available_gymhall(request):
    return render_to_response('ManageResources/view_available_gymhall.html', context_instance=RequestContext(request))

