from django.conf.urls.defaults import *

from ResourceBook.PlaceOrder import placeOrderViews

urlpatterns = patterns('', 
    
    url(r'^place_order/$', placeOrderViews.Place_order, name='Place_order')  
)