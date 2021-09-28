from django.contrib import admin
from .models import Comment



class CommentAdmin(admin.ModelAdmin):
    list_display = ['title','text','status','date']
    list_filter = ['status']


admin.site.register(Comment,CommentAdmin)