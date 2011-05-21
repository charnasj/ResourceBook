from django.views.generic.list_detail import object_list
from django.views.generic.list_detail import object_detail
from django.views.generic.create_update import create_object
from django.views.generic.create_update import update_object
from django.views.generic.create_update import delete_object
from django.core.urlresolvers import reverse
 
from models import *
from django.http import HttpRequest, HttpResponse
from django.shortcuts import render_to_response


def LocalGovernment_list(request):
    """Show all notes"""
 
    return object_list(request, 
        queryset=LocalGovernment.objects.all(),
        template_name='ManageResources/list.html',
        template_object_name='LocalGovernment'
    )
    
def LocalGovernment_detail(request, id, message):
    
    return object_detail(request,
        queryset=LocalGovernment.objects.all(),
        object_id=id,
        object_message=message,
        template_name='ManageResources/detail.html',
        template_object_name='LocalGovernment'
    )

    
	def Order_list(request):
    
    return object_list(request, queryset=Resource.objects.all(), template_name='ManageResources/orderDetail.html', template_object_name='LocalGovernment'
)

def index(request):
    return HttpResponse("This is an eGovernment platform for resource management.")

def Reg_newuser_save(request):
    if 'firstName' in request.GET and request.GET['firstName']:
        firstName= request.GET['firstName']
    if 'lastName' in request.GET and request.GET['lastName']:
        lastName= request.GET['lastName']
        new_user = User(first_name=firstName, last_name=lastName)
    #new_user = User(first_name="Mahammat" , last_name="Petrov")

    new_user.save()
    #return render_to_response('see_my_post.html', {'my_comment' : my_comment})
    return HttpResponse("A new User has been saved!")

def Reg_newuser_form(request):
   # if 'firstName' in request.GET and request.GET['firstName']:
    #    firstName= request.GET['firstName']
    #if 'lastName' in request.GET and request.GET['lastName']:
    #    lastName= request.GET['lastName']
#    new_user = User(first_name=firstName, last_name=lastName)

    #return render_to_response('see_my_post.html', {'my_comment' : my_comment})
    return render_to_response('ManageResources/new_user.html')
