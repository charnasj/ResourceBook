from django.conf.urls.defaults import *
import availabilityGoodsViews

urlpatterns = patterns('', 
    
    url(r'^view_available_goods/$', availabilityGoodsViews.View_available_goods, name='View_available_goods')
    
)