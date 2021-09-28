from django.contrib import admin
from .models import *

class CoursesAdmin(admin.ModelAdmin):
    list_filter = ['course','CourseSlug']

admin.site.register(Courses,CoursesAdmin)
admin.site.register(Students)
admin.site.register(Videos)
admin.site.register(IntroductionVideo)
