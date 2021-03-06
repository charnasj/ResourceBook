from django.conf.urls.defaults import *

import views
import addResourcesGoods
import addgymhall

import availabilityGoodsViews
import availabilityOrderView
from ResourceBook.ManageResources import userLogin,userRegistration

import PlaceGoodsOrder

from django.conf import settings

import availabilityGoodsViews
import viewProfile
import availabilityGymHallViews
import resource


urlpatterns = patterns('',

    url(r'^static/(?P<path>.*)$', 'django.views.static.serve', {'document_root': settings.MEDIA_ROOT, 'show_indexes': False}),
    url(r'^list/$', views.LocalGovernment_list, name='LocalGovernment_list'),

    url(r'^index/$', views.index, name='index'),
    url(r'^view_available_goods/$', availabilityGoodsViews.View_available_goods, name='View_available_goods'),
    url(r'^view_profile/$', viewProfile.View_Profile, name='View_Profile'),

    url(r'^view_order/$', availabilityOrderView.View_available_orders, name='View_order'),

    url(r'^detail/(?P<id>\d+)/$', views.LocalGovernment_detail, name='LocalGovernment_detail'),
    url(r'^add_gymhall/save_resource_gymhall/$', addgymhall.Add_resource_gymhall_save, name='Add_resource_gymhall_save'),
    url(r'^add_gymhall/$', addgymhall.Add_resource_gymhall_form, name='Add_resource_gymhall_form'),

	url(r'^place_gym_order_manager/save_resource_gymhall/$', addgymhall.Add_resource_gymhall_save, name='Add_resource_gymhall_save'),
	url(r'^place_gym_order_manager/$', addgymhall.Add_resource_gymhall_form, name='Add_resource_gymhall_form'),

    url(r'^add_resources_goods/add_resources_goods/$', addResourcesGoods.Add_resources_goods_save, name='Add_resources_goods_save'),
    url(r'^add_resources_goods/$', addResourcesGoods.Add_resources_goods_form, name='Add_resources_goods_form'),
    url(r'^new_user/save_user/$', userRegistration.Reg_newuser_save, name='Reg_newuser_save'),
    url(r'^new_user/$', userRegistration.Reg_newuser_form, name='Reg_newuser_form'),
    url(r'^login/$', userLogin.login_form, name='Login'),
    url(r'^login_succeed/$', userLogin.login_view, name='Login Succeed'),
    url(r'^logout', userLogin.logout_view, name='Logout'),
    url(r'^resource', resource.Resource_detai, name='Resource_detail'),


    url(r'^detail/(?P<id>\d+)/$', views.LocalGovernment_detail, name='LocalGovernment_detail'),
    url(r'^detail_goods/(?P<id>\d+)/$', views.Goods_details, name='Goods_details'),
    url(r'^detail_rent/(?P<id>\d+)/$', views.Rent_details, name='Rent_details'),
    url(r'^detail_rent/(?P<id>\d+)/place_gym_order/$', views.Place_gym_order, name='Place_gym_order'),
    
    
    
	url(r'^place_gym_order_manager/save_resource_gymhall/$', addgymhall.Add_resource_gymhall_save, name='Add_resource_gymhall_save'),
	url(r'^place_gym_order_manager/$', addgymhall.Add_resource_gymhall_form, name='Add_resource_gymhall_form'),

    url(r'^detail/(?P<id>\d+)/$', views.LocalGovernment_detail, name='LocalGovernment_detail'),
	url(r'^view_available_gymhall/$', availabilityGymHallViews.View_available_gymhall, name='View_available_gymhall'),
	url(r'^add_resources_gymhall/save_resource_gymhall/$', addgymhall.Add_resource_gymhall_save, name='Add_resource_gymhall_save'),
	url(r'^add_resources_gymhall/$', addgymhall.Add_resource_gymhall_form, name='Add_resource_gymhall_form'),

    url(r'^place_order_goods/$', PlaceGoodsOrder.Place_order_goods_save, name='Place_order_goods_save'),


    
    url(r'^place_goods_order/$', PlaceGoodsOrder.Place_order_goods_form, name='Place_order_goods_form'),
    url(r'^save_goods_order/$', PlaceGoodsOrder.Place_order_goods_save, name='Place_order_goods_save')
)
