from django.contrib import admin
from .models import Code

class CodeAdmin(admin.ModelAdmin):
    list_filter = ['status']

admin.site.register(Code,CodeAdmin)
