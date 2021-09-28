from django.contrib import admin
from .models import *


class DigitalAdmin(admin.ModelAdmin):
    search_fields = ['cart','product','price']
    list_display = ['cart','product','price','payment_date']
    list_filter = ['is_paid']

class PhysicalAdmin(admin.ModelAdmin):
    search_fields = ['cart','product','price','address']
    list_display = ['cart','product','price','payment_date','post_status','address']
    list_filter = ['post_status']
    list_filter = ['is_paid','post_status']

class CoursesAdmin(admin.ModelAdmin):
    search_fields = ['cart','course','price']
    list_display = ['cart','course','price','payment_date']
    list_filter = ['is_paid']

class CartAdmin(admin.ModelAdmin):
    search_fields = ['payment_date']
    list_display = ['owner','payment_date','is_paid']
    list_filter = ['is_paid']

admin.site.register(Digital,DigitalAdmin)
admin.site.register(Physical,PhysicalAdmin)
admin.site.register(Course,CoursesAdmin)
admin.site.register(Cart,CartAdmin)

