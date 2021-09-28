from django.urls import path
from .views import blog_page,showBlog_page

app_name = 'blog'

urlpatterns = [
    path('',blog_page,name='blogs_page'),
    path('<slug>',showBlog_page,name='showBlog_page'),
]