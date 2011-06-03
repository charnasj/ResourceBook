import uuid

from django.template import RequestContext
from django.shortcuts import get_object_or_404
from django.core.urlresolvers  import reverse
from django.conf import settings
#from paypal.standard.forms import PayPalPaymentsForm
from ManageResources.models import Resource
from django.template import RequestContext

def Resource_detai (request):
    
    paypal = {
         'amount':"1999",
         'item_name':"kgfgfhj",
         
         'invoice':str(uuid.uuid1()), 
         'return_url': settings.SITE_DOMAIN + reverse('http://localhost:8000'),
         'cancel_return':settings.SITE_DOMAIN + reverse('http://localhost:8000'),
             
              
              }
    form = PayPalPaymentsForm(initial=paypal)
    if settings.DEBUG:
        rendred_form = form.sandbox()
    else:
        rendred_form = form.render()
    return render_to_response ('ManageResources/Resource_detail.html', {
                                                        
           'Resource' : Resource,
           'form' : rendred_form,},RequestContext(request))        
    
