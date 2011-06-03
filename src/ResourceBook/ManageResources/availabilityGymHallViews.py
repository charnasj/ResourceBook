from django.views.generic.list_detail import object_list
from django.views.generic.list_detail import object_detail
from django.views.generic.create_update import create_object
from django.views.generic.create_update import update_object
from django.views.generic.create_update import delete_object
from django.core.urlresolvers import reverse
 
from django.http import HttpRequest, HttpResponse
from django.shortcuts import render_to_response
from ResourceBook.ManageResources.models import RentResource
from ResourceBook.ManageResources.models import Resource
from django.template import RequestContext


def View_available_gymhall(request):
    queryset=RentResource.objects.all()

    return render_to_response('ManageResources/view_available_gymhall.html' , {'gymhall':queryset},context_instance=RequestContext(request))


    
def View_available_gymhall_detail(request, id):
    
    return object_detail(request,
        queryset=RentResource.objects.all(),
        object_id=id,
        template_name='ViewAvailableGymhall/detail.html',
        template_object_name='ViewAvailableGymhall',
        context_instance=RequestContext(request)
    )

def index(request):
    return render_to_response('ManageResources/index.html',context_instance=RequestContext(request))

