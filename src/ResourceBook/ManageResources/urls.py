from django.conf.urls.defaults import *

import views
import addResourcesGoods
import addgymhall
import availabilityGoodsViews
import availabilityOrderView


urlpatterns = patterns('', 
    
    url(r'^list/$', views.LocalGovernment_list, name='LocalGovernment_list'),
    url(r'^index/$', views.index, name='index'),
    url(r'^view_available_goods/$', availabilityGoodsViews.View_available_goods, name='View_available_goods'),
    url(r'^view_order/$', availabilityOrderView.View_available_orders, name='View_order'),
    url(r'^add_resources_goods/add_resources_goods/$', addResourcesGoods.Add_resources_goods_save, name ='Add_resources_goods_save'),
    url(r'^add_resources_goods/$', addResourcesGoods.Add_resources_goods_form, name ='Add_resources_goods_form'),
#    url(r'^new_user/save_user/$', userRegistration.Reg_newuser_save, name='Reg_newuser_save'),
#    url(r'^new_user/$', userRegistration.Reg_newuser_form, name='Reg_newuser_form'),  
    url(r'^detail/(?P<id>\d+)/$', views.LocalGovernment_detail, name='LocalGovernment_detail'),
	url(r'^place_gym_order_manager/save_resource_gymhall/$', addgymhall.Add_resource_gymall_save, name='Add_resource_gymall_save'),
	url(r'^place_gym_order_manager/$', addgymhall.Add_resource_gymall_form, name='Add_resource_gymall_form'),
)