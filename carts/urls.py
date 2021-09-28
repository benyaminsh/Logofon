from django.urls import path
from .views import *

app_name = 'cart'

urlpatterns = [
    path('',cart_page,name='cart_page'),
    path('delete-order/<int:product_id>',deleteOrder_page,name='deleteOrder_page'),
]