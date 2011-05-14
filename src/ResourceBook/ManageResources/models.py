from django.db import models

# Create your models here.

class LocalGovernment (models.Model):
    name = models.CharField(max_length=70)
    address = models.TextField()
    phone = models.CharField(max_langth=13)

class User (models.Model):
    first_name = models.CharField(max_length=70)
    last_name = models.CharField(max_length=70)
    address = models.CharField(max_length=70)
    email = models.CharField(max_length=70)
    phone = models.CharField(max_length=13)    
    # TODO : User login/password ?

class VAT (models.Model):
    ratio = models.DecimalField()
    name = models.CharField(max_length=70)
    description = models.CharField(max_length=70)
    activityStart = models.DateTimeField()
    activityEnd = models.DateTimeField()
    next = models.IntegerField() # VAT ID link...

class Customer (User):
    shipping_address = models.CharField(max_length=70)
    
class ResourceManager (User):
    description = models.CharField(max_length=70)
    
    
class Resource (models.Model):
    name = models.CharField(max_length=70)
    description = models.CharField(max_length=70)
    unit_price = models.CharField(max_length=70)
    local_government_id = models.ForeignKey(LocalGovernment)
    vat_id = models.ForeignKey(VAT)

    
class Invoice (models.Model):
    total = models.BigIntegerField()
    totalExcl = models.BigIntegerField()
    totalVat = models.BigIntegerField()
    totalIncl = models.BigIntegerField()
    round = models.BigIntegerField()
    invoiceDate = models.DateTimeField()
    paymentDate = models.DateTimeField()
    PAYMENT_TYPES = (
     (u'PP',u'PayPal' ),
     (u'CC',u'Credit Card')
     )
    paymentKind = models.CharField(maxe_length=2, choices=PAYMENT_TYPES)
    
class InvoiceLine (models.Model):
    name = models.CharField(max_length=70)
    description = models.CharField(max_length=70)
    dueDate = models.DateTimeField()
    units = models.IntegerField()
    amount = models.BigIntegerField()
    total = models.BigIntegerField()
    totalExcl = models.BigIntegerField()
    totalIncl = models.BigIntegerField()
    periodStart = models.DateTimeField()
    periodEnd = models.DateTimeField()
    vat_id = models.ForeignKey(VAT)

class Order (models.Model):
    order_date = models.DateTimeField()
    status = models.CharField(max_length=70)
    customer_id = models.ForeignKey(Customer)
    invoice_id = models.ForeignKey(Invoice)

class OrderItem (models.Model):
    name = models.CharField(max_length=70)
    description = models.CharField(max_length=70) 
    unit_price = models.DecimalField()
    order_id = models.ForeignKey(Order)
    resource_id = models.ForeignKey(Resource)
    invoice_line_id = models.ForeignKey(InvoiceLine)

class GoodsResource (Resource):
    remaining_quantity = models.PositiveIntegerField()
    unit_type = models.CharField(max_length=70) # to display
    
class RentResource (Resource):
    address = models.TextField()
    
    
class RentReservation (models.Model):
    start = models.DateTimeField()
    finish = models.DateTimeField()
    rent_resource_id = models.ForeignKey(RentResource)
    customer_id = models.ForeignKey(User)
    order_item_id = models.ForeignKey(OrderItem)
    
class GoodsOrderItem (OrderItem):
    quantity = models.PositiveIntegerField()

class RentsOrderItem (OrderItem):
    start = models.DateTimeField()
    finish = models.DateTimeField()
    