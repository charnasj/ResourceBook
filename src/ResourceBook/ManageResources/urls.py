from django.conf.urls.defaults import *

import views

urlpatterns = patterns('', 
    
    url(r'^list/$', views.LocalGovernment_list, name='LocalGovernment_list'),
    url(r'^new_user/save_user/$', views.Reg_newuser_save, name='Reg_newuser_save'),
    url(r'^new_user/$', views.Reg_newuser_form, name='Reg_newuser_form'),  
    url(r'^detail/(?P<id>\d+)/$', views.LocalGovernment_detail, name='LocalGovernment_detail'),
    url(r'^list/$', views.Resource_list, name='Resource_list'),

)