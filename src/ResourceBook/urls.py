from django.conf.urls.defaults import *
from django.contrib import admin
admin.autodiscover()

from django.views.generic.simple import direct_to_template

urlpatterns = patterns('',
    # Examples:

    # url(r'^$', 'ResourceBook.views.home', name='home'),
    # url(r'^ResourceBook/', include('ResourceBook.foo.urls')),

    # Uncomment the admin/doc line below to enable admin documentation:
    # url(r'^admin/doc/', include('django.contrib.admindocs.urls')),
    # url(r'^accounts/', include('registration.backends.default.urls')),
    # Uncomment the next line to enable the admin:
    url(r'^admin/', include(admin.site.urls)),
    url(r'^AvailabilityGoods/', include('AvailabilityGoods.urls')),
    url(r'^ManageResources/$','ManageResources.views.index'),
    url(r'^ManageResources/', include('ManageResources.urls')),
    url(r'^PlaceOrder/', include('PlaceOrder.urls')),
#    url(r'^AvailabilityGoods/', include('AvailabilityGoods.urls'))
)
