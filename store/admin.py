from django.contrib import admin
from .models import Product
from .models import Category
from .models import Customer
from .models import Orders


class AdminProduct(admin.ModelAdmin):
    list_display=['name','price','category']

class AdminCategory(admin.ModelAdmin):
    list_display=['name']

class AdminCustomer(admin.ModelAdmin):
    list_display=['name','mobile','email','password']

class AdminOrders(admin.ModelAdmin):
    list_display=['product','customer','quantity','price','date']

# Register your models here.
admin.site.register(Product,AdminProduct)
admin.site.register(Category,AdminCategory)
admin.site.register(Customer,AdminCustomer)
admin.site.register(Orders,AdminOrders)