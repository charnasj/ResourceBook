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
        template_object_name='RentResource'
    )

def Place_gym_order(request, id):
    now = datetime.datetime.now()
    print(now)
    JSON_time = 'Wed Apr 21 19:29:07 +0000 2010'
    my_time = datetime.datetime.strptime(JSON_time, '%a %b %d %H:%M:%S +0000 %Y')
    m_t="03/06/11"
#    'YYYY-MM-DD HH:MM[:ss[.uuuuuu]]'
    mahamat_time = datetime.datetime.strptime(m_t, "%d/%m/%y")
    print(now.strftime("%d/%m/%y"))
    print(mahamat_time)
    print("AAAAAAAAAAAAAAAA")
    print(my_time)
#    name = models.CharField(max_length=70)
#    description = models.CharField(max_length=70) 
#    unit_price = models.DecimalField(decimal_places=2,max_digits=10)
#    order_id = models.ForeignKey(Order)
#    resource_id = models.ForeignKey(Resource)
#    invoice_line_id = models.ForeignKey(InvoiceLine)
    new_RentsOrderItem = RentsOrderItem(name="New Rents Order", description = "Some description", start = mahamat_time
                                        ,unit_price=30, order_id_id=1, resource_id_id=1, invoice_line_id_id=1)
    new_RentsOrderItem.save()
    return HttpResponse("keep it simple")


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

