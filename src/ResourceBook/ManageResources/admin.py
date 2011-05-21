from models import *
from django.contrib import admin

class LocalGovernmentAdmin(admin.ModelAdmin):
    list_display = ['name', 'address', 'phone']
admin.site.register(LocalGovernment, LocalGovernmentAdmin)
 
class UserAdmin(admin.ModelAdmin):
    list_display = ['first_name' , 'last_name' , 'address']
admin.site.register(User, UserAdmin)

class VATAdmin(admin.ModelAdmin):
    list_display = ['name' , 'ratio' , 'description']
admin.site.register(VAT, VATAdmin)

class CustomerAdmin(admin.ModelAdmin):
    list_display = ['shipping_address']
admin.site.register(Customer, CustomerAdmin)

class ResourceManagerAdmin(admin.ModelAdmin):
    list_display = ['description']
admin.site.register(ResourceManager, ResourceManagerAdmin)

class ResourceAdmin(admin.ModelAdmin):
    list_display = ['name', 'description', 'unit_price']
admin.site.register(Resource, ResourceAdmin)

class InvoiceAdmin(admin.ModelAdmin):
    list_display = ['total', 'totalIncl', 'invoiceDate']
admin.site.register(Invoice, InvoiceAdmin)

class InvoiceLineAdmin(admin.ModelAdmin):
    list_display = ['name', 'description', 'amount', 'totalIncl']
admin.site.register(InvoiceLine, InvoiceLineAdmin)

class OrderAdmin(admin.ModelAdmin):
    list_display = ['order_date', 'status']
admin.site.register(Order, OrderAdmin)

class OrderItemAdmin(admin.ModelAdmin):
    list_display = ['name', 'description', 'unit_price']
admin.site.register(OrderItem, OrderItemAdmin)

class GoodsResourceAdmin(admin.ModelAdmin):
    list_display = ['name','description','remaining_quantity', 'unit_type']
admin.site.register(GoodsResource, GoodsResourceAdmin)

class RentResourceAdmin(admin.ModelAdmin):
    list_display = ['address']
admin.site.register(RentResource, RentResourceAdmin)

class RentReservationAdmin(admin.ModelAdmin):
    list_display = ['start', 'finish']
admin.site.register(RentReservation, RentReservationAdmin)

class GoodsOrderItemAdmin(admin.ModelAdmin):
    list_display = ['quantity']
admin.site.register(GoodsOrderItem, GoodsOrderItemAdmin)

class RentsOrderItemAdmin(admin.ModelAdmin):
    list_display = ['start', 'finish']
admin.site.register(RentsOrderItem, RentsOrderItemAdmin)