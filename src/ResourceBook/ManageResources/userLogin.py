from django.contrib.auth import authenticate, login, logout
from django.http import HttpResponse
from django.shortcuts import render_to_response    

def login_view(request):
    username = request.POST['username']
    password = request.POST['password']
    user = authenticate(username=username, password=password)
    if user is not None:
        if user.is_active:
            login(request, user)
            return HttpResponse("You provided a correct username and password!")
        else:
            return HttpResponse("Your account has been disabled!")

def logout_view(request):
    logout(request)
    return HttpResponse("Successfully logged out. See you again soon!")

def login_form(request):
    return render_to_response('ManageResources/login.html')
