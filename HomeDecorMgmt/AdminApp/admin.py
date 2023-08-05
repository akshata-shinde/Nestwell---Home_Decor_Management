from django.contrib import admin
from .models import Product,Category,Payment

# Register your models here.
class CategoryAdmin(admin.ModelAdmin):
    list_display = ("id","category_name")


class ProductAdmin(admin.ModelAdmin):
    list_display = ("id","product_name","price","size","description","image","category")

class PaymentAdmin(admin.ModelAdmin):
    list_display = ("id","card_no","cvv","expiry","balance")

admin.site.register(Category,CategoryAdmin)
admin.site.register(Product,ProductAdmin)
admin.site.register(Payment,PaymentAdmin)