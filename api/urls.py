from django.urls import path
from .views import *

app_name = 'api'

urlpatterns = [
    path('addOrder/',addOrder,name='addOrder'),
    path('deleteOrder/',deleteOrder,name='deleteOrder'),
    path('addCourses/',addCourses,name='addCourses'),
    path('deleteCourses/',deleteCourses,name='deleteCourses'),
    path('number/',number,name='number'),
    path('list/',list,name='list'),
    path('discountCode/',discountCode,name='discountCode'),
]