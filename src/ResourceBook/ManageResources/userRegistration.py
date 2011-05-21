from models import *
from django.http import HttpRequest, HttpResponse
from django.shortcuts import render_to_response



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
    
    new_user = User(first_name=firstName,last_name=lastName,username=username,
                                password=password,address=address,email=email,phone=phone)
    #new_user.user.email_user("Welcome to ResourceBook!", registration_mail_content, from_email)
    new_user.save()
    
    return HttpResponse("A new User has been saved!")

def Reg_newuser_form(request):
   # if 'firstName' in request.GET and request.GET['firstName']:
    #    firstName= request.GET['firstName']
    #if 'lastName' in request.GET and request.GET['lastName']:
    #    lastName= request.GET['lastName']
#    new_user = User(first_name=firstName, last_name=lastName)

    #return render_to_response('see_my_post.html', {'my_comment' : my_comment})
    return render_to_response('ManageResources/new_user.html')