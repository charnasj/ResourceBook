from django.db import models

# Create your models here.

class User (models.Model):
    first_name = models.CharField(max_length=70)
    last_name = models.CharField(max_length=70)
    adresse = models.CharField(max_length=70)
    email = models.CharField(max_length=70)    

class Customer (User):
    adresse2 = models.CharField(max_length=70)
    
class ResourceManager (User):
    resource = models.CharField(max_length=70)
    

class Order (models.Model):
    order_date = models.DateTimeField()
    status = models.CharField(max_length=70)
    advance = models.CharField(max_length=70)
    payed = models.CharField(max_length=70)
    
class GoodsOrder (Order):
    

class RentsOrder (Order):
    

class Invoice (models.Model):


class OrderItem (models.Model):
    
class InvoiceLine (models.Model):
    
class VAT (models.Model):
    
class LocalGovernment (models.Model):
    
class RentReservation (models.Model):


class Resource (models.Model):
    description = models.TextField()
    Price = models.CharField(max_length=70)

class GoodsResource (Resource):
    quantity = models.CharField(max_length=70)
    
class RentsResource (Resource):
    