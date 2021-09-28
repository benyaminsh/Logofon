from django.urls import path
from .views import *

app_name = 'payment'

urlpatterns = [
    path('Factor/', Factor_page, name='Factor_page'),
    path('request/', send_request, name='request_page'),
    path('verify/', verify , name='verify_page'),
]
