from django.contrib import admin
from .models import Product


class ProductAdmin(admin.ModelAdmin):
    list_filter = ['slug','title']


admin.site.register(Product,ProductAdmin)
