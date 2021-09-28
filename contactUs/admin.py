from django.contrib import admin
from .models import ContactUs

class ContactUsAdmin(admin.ModelAdmin):
    list_filter = ['status']


admin.site.register(ContactUs,ContactUsAdmin)
