from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import User

UserAdmin.fieldsets[1][1]['fields'] = ('first_name','last_name','gender','news','phone','phone_authentication','block','user_photo')

UserAdmin.list_filter = ['gender']

UserAdmin.list_display = ['username','first_name','first_name','phone','phone_authentication','block']

UserAdmin.search_fields = ['username','first_name','first_name','phone']

admin.site.register(User,UserAdmin)