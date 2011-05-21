from django.views.generic.list_detail import object_list
from django.views.generic.list_detail import object_detail
from django.views.generic.create_update import create_object
from django.views.generic.create_update import update_object
from django.views.generic.create_update import delete_object
from django.core.urlresolvers import reverse
 
from models import *
from django.http import HttpRequest, HttpResponse
from django.shortcuts import render_to_response

def Reg_newuser_save(request):
    if 'firstName' in request.GET and request.GET['firstName']:
        firstName= request.GET['firstName']
    if 'lastName' in request.GET and request.GET['lastName']:
        lastName= request.GET['lastName']
    if 'password' in request.GET and request.GET['password']:
        password= request.GET['password']
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