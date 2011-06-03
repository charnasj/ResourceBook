from django.contrib.auth import authenticate, login, logout
from django.http import HttpResponse
from django.shortcuts import render_to_response
from models import *

def login_view(request):
    username = request.GET['username']
    password = request.GET['password']
    if request.session.__contains__('user_id'):
        del request.session['user_id']
    user = authenticate(username=username, password=password)
    if user is not None:
        if user.is_active:
            login(request, user)
            request.session['user_id'] = user.id
            if user.is_staff == 0 and not request.session.__contains__('customer_id'):
                request.session['customer_id'] = ResourceBookUser.objects.get(user = user.id).id 
                print request.session['customer_id'] 
            print request.session['user_id']
            return render_to_response('ManageResources/login_succeed.html')
        else:
            return HttpResponse("Your account has been disabled!")
    else:
        return render_to_response('ManageResources/login_failed.html')

def logout_view(request):
    logout(request)
    response = HttpResponse("Successfully logged out. See you again soon!")
    del request.session['user_id']
    if request.session['customer_id'] is not None:
        del request.session['customer_id']
    return response

def login_form(request):
    return render_to_response('ManageResources/login.html')
