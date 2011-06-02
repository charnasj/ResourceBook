from django.conf.urls.defaults import *

import views
import addResourcesGoods

from ResourceBook.ManageResources import userLogin,userRegistration
import addgymhall
import availabilityGoodsViews
import availabilityGymHallViews


urlpatterns = patterns('',
    
    url(r'^list/$', views.LocalGovernment_list, name='LocalGovernment_list'),
    url(r'^index/$', views.index, name='index'),
    url(r'^view_available_goods/$', availabilityGoodsViews.View_available_goods, name='View_available_goods'),
    url(r'^add_resources_goods/add_resources_goods/$', addResourcesGoods.Add_resources_goods_save, name='Add_resources_goods_save'),
    url(r'^add_resources_goods/$', addResourcesGoods.Add_resources_goods_form, name='Add_resources_goods_form'),
    url(r'^new_user/save_user/$', userRegistration.Reg_newuser_save, name='Reg_newuser_save'),
    url(r'^new_user/$', userRegistration.Reg_newuser_form, name='Reg_newuser_form'),
    url(r'^login', userLogin.login_form, name='Login_form'),
    url(r'^login_succeed', userLogin.login_view, name='Login_succeed'),
    url(r'^logout', userLogin.logout_view, name='Logout'),
    url(r'^detail/(?P<id>\d+)/$', views.LocalGovernment_detail, name='LocalGovernment_detail'),
	url(r'^view_available_gymhall/$', availabilityGymHallViews.View_available_gymhall, name='View_available_gymhall'),
	url(r'^add_resources_gymhall/save_resource_gymhall/$', addgymhall.Add_resource_gymall_save, name='Add_resource_gymall_save'),
	url(r'^add_resources_gymhall/$', addgymhall.Add_resource_gymall_form, name='Add_resource_gymall_form'),
)
