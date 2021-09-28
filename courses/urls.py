from django.urls import path
from .views import *

app_name = 'courses'

urlpatterns = [
    path('',courses_page,name='courses_page'),
    path('<int:id>/',ShowCourse_page,name='ShowCourse_page')
]