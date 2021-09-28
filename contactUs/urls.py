from django.urls import path
from .views import contactus_page

app_name = 'contact'

urlpatterns = [
    path('',contactus_page,name='contactus_page')
]