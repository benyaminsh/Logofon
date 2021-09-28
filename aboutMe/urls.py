from django.urls import path
from .views import aboutDr

app_name = 'aboutMe'

urlpatterns = [
    path('',aboutDr,name='aboutDr')
]