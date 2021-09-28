from django.urls import path
from .views import *

app_name = 'news'

urlpatterns = [
    path('',news_page,name='news_page')
]