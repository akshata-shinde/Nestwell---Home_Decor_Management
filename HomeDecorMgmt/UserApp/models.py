from django.db import models
from AdminApp.models import Product
from datetime import datetime

# Create your models here.
class UserInfo(models.Model):
    username = models.CharField(max_length=30, primary_key=True)
    password = models.CharField(max_length=20)

    class Meta:
        db_table = "UserInfo"

class MyCart(models.Model):
    user = models.ForeignKey(UserInfo,on_delete=models.CASCADE)
    product = models.ForeignKey(Product,on_delete=models.CASCADE)
    qty = models.IntegerField(default=1)

    class Meta:
        db_table = "MyCart"

class OrderMaster(models.Model):
    user = models.ForeignKey(UserInfo,on_delete=models.CASCADE)
    date_of_order = models.DateField(default = datetime.now)
    amount = models.FloatField(default=1000)
    details = models.CharField(max_length=200)

    class Meta:
        db_table = "OrderMaster"
        