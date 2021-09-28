from django.urls import path
from .views import *

app_name = 'userPanel'

urlpatterns = [
    path('',userPanel_page,name='userPanel_page'),
    path('changePassword/',changePassword_page,name='changePassword_page'),
    path('changeProfile/',changeProfile_page,name='changeProfile_page'),
    path('digitalProducts/',digitalProducts_page,name='digitalProducts_page'),
    path('physicalProducts/',physicalProducts_page,name='physicalProducts_page'),
    path('courses/',courses_page,name='courses_page'),
    path('approvedComments/',approvedComments_page,name='approvedComments_page'),
    path('unapprovedComments/',unapprovedComments_page,name='unapprovedComments_page'),

]