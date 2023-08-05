from django.db import models

# Create your models here.

class Category(models.Model):
    category_name = models.CharField(max_length=30)
    
    def __str__(self):
        return self.category_name
    
    class Meta:
        db_table = "Category"

    
class Product(models.Model):
    product_name = models.CharField(max_length=100)
    price = models.FloatField(default=2000)
    size = models.CharField(max_length=100)
    description = models.CharField(max_length=800)
    image = models.ImageField(upload_to="images",default="abc.jpg")
    category = models.ForeignKey(Category,on_delete=models.CASCADE)
   
    class Meta:
        db_table = "Product"

class Payment(models.Model):
    card_no = models.CharField(max_length=4)
    cvv =  models.CharField(max_length=4)
    expiry =  models.CharField(max_length=10)
    balance = models.FloatField(default=10000)

    class Meta:
        db_table = "Payment"