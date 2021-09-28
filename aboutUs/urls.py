from django.urls import path
from .views import aboutus_page

app_name = 'aboutUs'

urlpatterns = [
    path('',aboutus_page,name='aboutus_page')
]