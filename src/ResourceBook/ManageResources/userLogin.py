from django.contrib.auth import authenticate, login, logout
from django.http import HttpResponse
from django.shortcuts import render_to_response    

def login_view(request):
    username = request.GET['username']
    password = request.GET['password']
    user = authenticate(username=username, password=password)
    if user is not None:
        if user.is_active:
            login(request, user)
            return render_to_response('ManageResources/login_succeed.html')
        else:
            return HttpResponse("Your account has been disabled!")
    else:
        return render_to_response('ManageResources/login_failed.html')

def logout_view(request):
    logout(request)
    response = HttpResponse("Successfully logged out. See you again soon!")
    return response

def login_form(request):
    return render_to_response('ManageResources/login.html')
