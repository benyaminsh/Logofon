from django.urls import path
from .views import *


app_name = 'product'

urlpatterns = [
    path('physicalProducts/',physicalProducts_page,name='physicalProducts_page'),
    path('digitalProducts/',digitalProducts_page,name='digitalProducts_page'),
    path('<slug>/',productDisplay_page,name='productDisplay_page'),
]