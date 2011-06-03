from django.contrib.auth import authenticate, login, logout
from django.http import HttpResponse
from django.shortcuts import render_to_response
from models import *
from django.template import RequestContext
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
            request.session['first_name'] = user.first_name
            if user.is_staff == 0 and not request.session.__contains__('customer_id'):
                request.session['customer_id'] = ResourceBookUser.objects.get(user = user.id).id 
            return render_to_response('ManageResources/login_succeed.html', context_instance=RequestContext(request))
        else:
            return HttpResponse("Your account has been disabled!",context_instance=RequestContext(request))
    else:
        return render_to_response('ManageResources/login_failed.html',context_instance=RequestContext(request))

def logout_view(request):
    logout(request)
    return render_to_response('ManageResources/logout.html',context_instance=RequestContext(request))

def login_form(request):
    return render_to_response('ManageResources/login.html',context_instance=RequestContext(request))
