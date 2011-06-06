from django.db import models
from django.contrib.auth.models import User
import datetime

class LocalGovernment (models.Model):
    name = models.CharField(max_length=70)
    address = models.TextField()
    phone = models.CharField(max_length=13)

class ResourceBookUser (models.Model):
    user = models.ForeignKey(User)
    address = models.CharField(max_length=70)
    phone = models.CharField(max_length=13)    

class VAT (models.Model):
#    ratio = models.DecimalField(decimal_places=2,max_digits=10)
    ratio = models.IntegerField()
    name = models.CharField(max_length=70)
    description = models.CharField(max_length=70)
    activityStart = models.DateTimeField()
    activityEnd = models.DateTimeField()
    next = models.IntegerField() # VAT ID link...


class Customer (ResourceBookUser):
    shipping_address = models.CharField(max_length=70)
    
class ResourceManager (ResourceBookUser):
    description = models.CharField(max_length=70)
    
    
class Resource (models.Model):
    name = models.CharField(max_length=70)
    description = models.CharField(max_length=70)
    unit_price = models.CharField(max_length=70)
    local_government_id = models.ForeignKey(LocalGovernment)
    vat_id = models.ForeignKey(VAT)

    
class Invoice (models.Model):
    total = models.BigIntegerField(null=True)
    totalExcl = models.BigIntegerField(null=True)
    totalVat = models.BigIntegerField(null=True)
    totalIncl = models.BigIntegerField(null=True)
    round = models.BigIntegerField(null=True)
    invoiceDate = models.DateTimeField(auto_now=True)
    paymentDate = models.DateTimeField(null=True)
    PAYMENT_TYPES = (
     (u'PP',u'PayPal' ),
     (u'CC',u'Credit Card')
     )
    paymentKind = models.CharField(max_length=2, choices=PAYMENT_TYPES,null=True)
    

class InvoiceLine (models.Model):
    name = models.CharField(max_length=70)
    description = models.CharField(max_length=70)
    dueDate = models.DateTimeField(auto_now=True)
    units = models.IntegerField(null=True)
    amount = models.BigIntegerField(null=True)
    total = models.BigIntegerField(null=True)
    totalExcl = models.BigIntegerField(null=True)
    totalIncl = models.BigIntegerField(null=True)
    periodStart = models.DateTimeField(auto_now=True)
    periodEnd = models.DateTimeField(auto_now=True)
    vat_id  = models.ForeignKey(VAT,null=True)
    #invoice_id = models.ForeignKey(Invoice)
    
    def save(self, *args, **kwargs):
        vat             = VAT.objects.get( id=self.vat_id.id )
        self.total      = long(self.units) * long(self.amount)
        self.totalExcl  = self.total
        vatTotal        = long(float(vat.ratio) * float(self.totalExcl))
        self.totalIncl  = long(self.totalExcl) + long(vatTotal)
        super(InvoiceLine, self).save(*args, **kwargs) # Call the "real" save() method.
        
class Order (models.Model):
    order_date = models.DateTimeField()
    status = models.CharField(max_length=70)
    customer_id = models.ForeignKey(Customer)
    invoice_id = models.ForeignKey(Invoice)
    
class OrderItem (models.Model):
    name = models.CharField(max_length=70)
    description = models.CharField(max_length=70) 
    unit_price = models.DecimalField(decimal_places=2,max_digits=10)
    order_id = models.ForeignKey(Order)
    resource_id = models.ForeignKey(Resource)
    #invoice_line_id = models.ForeignKey(InvoiceLine)
    
    def save(self, *args, **kwargs):
        targetResource       = Resource.objects.get( id=self.resource_id.id )
        self.name            = targetResource.name
        self.description     = targetResource.description
        self.unit_price      = targetResource.unit_price
        super(OrderItem, self).save(*args, **kwargs) # Call the "real" save() method.
        
class GoodsResource (Resource):
    remaining_quantity = models.PositiveIntegerField()
    unit_type = models.CharField(max_length=70) # to display
    
class RentResource (Resource):
    address = models.TextField()
    
class RentReservation (models.Model):
    start = models.DateTimeField()
    finish = models.DateTimeField()
    rent_resource_id = models.ForeignKey(RentResource)
    customer_id = models.ForeignKey(ResourceBookUser)
    order_item_id = models.ForeignKey(OrderItem)
    
class GoodsOrderItem (OrderItem):
    quantity = models.PositiveIntegerField()
        
class RentsOrderItem (OrderItem):
    start = models.CharField(max_length=20)
    finish = models.CharField(max_length=20)
    