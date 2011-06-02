from django.conf.urls.defaults import *

import views
import userRegistration
import addResourcesGoods
import addgymhall
import PlaceGoodsOrder

from django.conf import settings

urlpatterns = patterns('', 
    url(r'^static/(?P<path>.*)$', 'django.views.static.serve', {'document_root': settings.MEDIA_ROOT, 'show_indexes': True}),
    url(r'^list/$', views.LocalGovernment_list, name='LocalGovernment_list'),
    url(r'^add_resources_goods/add_resources_goods/$', addResourcesGoods.Add_resources_goods_save, name ='Add_resources_goods_save'),
    url(r'^add_resources_goods/$', addResourcesGoods.Add_resources_goods_form, name ='Add_resources_goods_form'),
    url(r'^new_user/save_user/$', userRegistration.Reg_newuser_save, name='Reg_newuser_save'),
    url(r'^new_user/$', userRegistration.Reg_newuser_form, name='Reg_newuser_form'),  
    url(r'^detail/(?P<id>\d+)/$', views.LocalGovernment_detail, name='LocalGovernment_detail'),
	url(r'^add_gymhall/save_resource_gymhall/$', addgymhall.Add_resource_gymall_save, name='Add_resource_gymall_save'),
	url(r'^add_gymhall/$', addgymhall.Add_resource_gymall_form, name='Add_resource_gymall_form'),
    url(r'^place_goods_order/$', PlaceGoodsOrder.getGoodsOrderForm, name='Place_goods_order'),
    url(r'^place_goods_order/create_order$', PlaceGoodsOrder.placeGoodsOrder, name='Place_goods_order_form'),
)