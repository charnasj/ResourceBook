from django.conf.urls.defaults import *

import views
import userRegistration

urlpatterns = patterns('', 
    
    url(r'^list/$', views.LocalGovernment_list, name='LocalGovernment_list'),
    url(r'^new_user/save_user/$', userRegistration.Reg_newuser_save, name='Reg_newuser_save'),
    url(r'^new_user/$', userRegistration.Reg_newuser_form, name='Reg_newuser_form'),  
    url(r'^detail/(?P<id>\d+)/$', views.LocalGovernment_detail, name='LocalGovernment_detail'),
	url(r'^add_gymhall/save_resource_gymhall/$', views.Add_resource_gymall_save, name='Add_resource_gymall_save'),
	url(r'^add_gymhall/$', views.Add_resource_gymall_form, name='Add_resource_gymall_form'),
)