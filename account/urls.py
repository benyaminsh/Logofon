from django.urls import path
from .views import *

app_name = 'account'

urlpatterns = [
    path('register/',register_page,name='register_page'),
    path('login/',login_page,name='login_page'),
    path('logout/',logout_page,name='logout_page'),
    path('code/',code_page,name='code_page'),
    path('',account_page, name='account_page'),
    path('passwordReset/',passwordReset_page, name='passwordReset_page'),
]