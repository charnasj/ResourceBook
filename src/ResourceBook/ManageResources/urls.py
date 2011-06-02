from django.conf.urls.defaults import *

import views
import addResourcesGoods

from ResourceBook.ManageResources import userLogin,userRegistration
import addgymhall
import PlaceGoodsOrder

from django.conf import settings

import availabilityGoodsViews
import viewProfile
import availabilityGymHallViews

urlpatterns = patterns('',
url(r'^static/(?P<path>.*)$', 'django.views.static.serve', {'document_root': settings.MEDIA_ROOT, 'show_indexes': True}),
    url(r'^list/$', views.LocalGovernment_list, name='LocalGovernment_list'),
    url(r'^add_resources_goods/add_resources_goods/$', addResourcesGoods.Add_resources_goods_save, name ='Add_resources_goods_save'),
    url(r'^add_resources_goods/$', addResourcesGoods.Add_resources_goods_form, name ='Add_resources_goods_form'),
    url(r'^new_user/save_user/$', userRegistration.Reg_newuser_save, name='Reg_newuser_save'),
    url(r'^new_user/$', userRegistration.Reg_newuser_form, name='Reg_newuser_form'),  
    url(r'^detail/(?P<id>\d+)/$', views.LocalGovernment_detail, name='LocalGovernment_detail'),
    url(r'^add_gymhall/save_resource_gymhall/$', addgymhall.Add_resource_gymhall_save, name='Add_resource_gymhall_save'),
    url(r'^add_gymhall/$', addgymhall.Add_resource_gymhall_form, name='Add_resource_gymhall_form'),
    url(r'^place_goods_order/$', PlaceGoodsOrder.getGoodsOrderForm, name='Place_goods_order'),
    url(r'^place_goods_order/create_order$', PlaceGoodsOrder.placeGoodsOrder, name='Place_goods_order_form'),
	url(r'^place_gym_order_manager/save_resource_gymhall/$', addgymhall.Add_resource_gymhall_save, name='Add_resource_gymhall_save'),
	url(r'^place_gym_order_manager/$', addgymhall.Add_resource_gymhall_form, name='Add_resource_gymhall_form'),
    url(r'^add_resources_goods/add_resources_goods/$', addResourcesGoods.Add_resources_goods_save, name='Add_resources_goods_save'),
    url(r'^add_resources_goods/$', addResourcesGoods.Add_resources_goods_form, name='Add_resources_goods_form'),
    url(r'^new_user/save_user/$', userRegistration.Reg_newuser_save, name='Reg_newuser_save'),
    url(r'^new_user/$', userRegistration.Reg_newuser_form, name='Reg_newuser_form'),
    url(r'^login', userLogin.login_form, name='Login_form'),
    url(r'^login_succeed', userLogin.login_view, name='Login_succeed'),
    url(r'^logout', userLogin.logout_view, name='Logout'),
    url(r'^detail/(?P<id>\d+)/$', views.LocalGovernment_detail, name='LocalGovernment_detail'),
	url(r'^view_available_gymhall/$', availabilityGymHallViews.View_available_gymhall, name='View_available_gymhall'),
	url(r'^add_resources_gymhall/save_resource_gymhall/$', addgymhall.Add_resource_gymhall_save, name='Add_resource_gymhall_save'),
	url(r'^add_resources_gymhall/$', addgymhall.Add_resource_gymhall_form, name='Add_resource_gymhall_form')
)
