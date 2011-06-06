from models import *
from django.http import HttpResponse
from django.shortcuts import render_to_response
from django.contrib.auth.models import User
from django.template import RequestContext


def Reg_newuser_save(request):
    #registration_mail_content = "Weclome to the ResourceBook Django platform!\nThis is an email to confirm that you have registered as a new user.\n if this wasn't you, please contact the administrator ASAP."
    #from_email = "egov-django@unine.ch"
    if 'firstName' in request.GET and request.GET['firstName']:
        firstName= request.GET['firstName']
    if 'lastName' in request.GET and request.GET['lastName']:
        lastName= request.GET['lastName']
    if 'username' in request.GET and request.GET['username']:
        username= request.GET['username']
    if 'password' in request.GET and request.GET['password']:
        password= request.GET['password']
    if 'address' in request.GET and request.GET['address']:
        address= request.GET['address']
    if 'email' in request.GET and request.GET['email']:
        email= request.GET['email']    
    if 'phone' in request.GET and request.GET['phone']:
        phone= request.GET['phone'] 
    
    auth_user = User(username=username,first_name=firstName, last_name=lastName,
                     email=email, is_staff=False,is_active=True,
                     is_superuser=False)
    auth_user.set_password(password)
    auth_user.save()
#    new_user = ResourceBookUser(address=address,phone=phone,user=auth_user)
    #new_user.user.email_user("Welcome to ResourceBook!", registration_mail_content, from_email)
#    new_user.save()
    new_customer = Customer(address=address,phone=phone,user=auth_user, shipping_address = address)
    new_customer.save()
    
    return HttpResponse("A new ResourceBookUser has been saved!")

def Reg_newuser_form(request):
    return render_to_response('ManageResources/new_user.html')