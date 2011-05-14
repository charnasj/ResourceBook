from django.conf.urls.defaults import *

import views

urlpatterns = patterns('', 
    
    url(r'^list/$', views.LocalGovernment_list, name='LocalGovernment_list'),  
    url(r'^detail/(?P<id>\d+)/$', views.LocalGovernment_detail, name='LocalGovernment_detail'),

)