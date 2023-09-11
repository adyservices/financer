from django.db import models
from accounts.models import CustomUser
# Create your models here.

PAYMENT_TYPE = (("EXPENCES", "EXPENCES"),("DONATIONS", "DONATIONS"))
PAYMENT_STATUS = (("FULL", "FULL"),("ADVANCED", "ADVANCED"),("PARTIAL", "PARTIAL"),("INITIADED", "INITIAD"))
PAYMENT_METHODS = (("CASH", "CASH"),("ONLINE", "ONLINE"))
class Payments(models.Model):
    payment_type = models.CharField(max_length=10,choices=PAYMENT_TYPE,default="EXPENCES")
    payment_status = models.CharField(max_length=10,choices=PAYMENT_STATUS,default="INITIADED")
    bill_name = models.CharField(max_length=100)
    bill_description = models.TextField(max_length=500)
    bill_paid_to = models.TextField(max_length=100)
    bill_received_by = models.TextField(max_length=100)
    bill_amount = models.IntegerField()
    paid_amount = models.IntegerField()
    active = models.BooleanField(default=True)

class Transactions(models.Model):
    payment_id = models.ForeignKey(Payments,on_delete=models.CASCADE)
    transacion_type = models.CharField(max_length=100,choices=PAYMENT_STATUS,default="ADVANCED")
    transaction_amount = models.IntegerField()
    payemnt_method = models.CharField(max_length=100,choices=PAYMENT_METHODS,default="CASH")
    receipt = models.CharField(max_length=357)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    created_by = models.ForeignKey(CustomUser,on_delete=models.CASCADE)
    active = models.BooleanField(default=True)



