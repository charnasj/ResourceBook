from django.conf.urls.defaults import *

import views

urlpatterns = patterns('', 
    
    url(r'^list/$', views.LocalGovernment_list, name='LocalGovernment_list'),
    url(r'^new_user/save_user/$', views.Reg_newuser_save, name='Reg_newuser_save'),
    url(r'^new_user/$', views.Reg_newuser_form, name='Reg_newuser_form'),
    url(r'^add_resources_goods/add_resources_goods/$', views.Add_resources_goods_save, name ='Add_resources_goods_save'),
    url(r'^add_resources_goods/$', views.Add_resources_goods_form, name ='Add_resources_goods_form'),
    url(r'^detail/(?P<id>\d+)/$', views.LocalGovernment_detail, name='LocalGovernment_detail'),

)