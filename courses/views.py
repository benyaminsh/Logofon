from django.shortcuts import render,redirect
from django.core.paginator import Paginator
from siteSettings.models import SiteSettings
from django.contrib import messages
from users.models import User
from carts.models import *
from .models import *



def courses_page(request):
    if request.user.is_authenticated:
        if request.user.phone_authentication != True:
            return redirect('account:code_page')
        else:
            user_info = User.objects.filter(username=request.user.username).first()
            
            if user_info.block == True:
                messages.error(request, 'اکانت شما مسدود شده است لطفا با پشتیبانی تماس بگیرید')
                return redirect('contact:contactus_page')
    else: return redirect('account:login_page')


    posts = Courses.objects.filter(CourseStatus=True).all()
    paginator = Paginator(posts, 9)
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)
    settings = SiteSettings.objects.last()
    title = settings.title + ' ' + '-' + ' ' + 'دوره ها'
    context = {
        'title': title,
        'posts': page_obj,
    }
    return render(request,'courses/courses_page/coursesPage.html',context)


def ShowCourse_page(request,id):
    if request.user.is_authenticated:
        if request.user.phone_authentication != True:
            return redirect('account:code_page')
        else:
            user_info = User.objects.filter(username=request.user.username).first()
            
            if user_info.block == True:
                messages.error(request, 'اکانت شما مسدود شده است لطفا با پشتیبانی تماس بگیرید')
                return redirect('contact:contactus_page')
    else: return redirect('account:login_page')

    cart = Course.objects.filter(course_id=id,is_paid=True).first()
    status = False
    if cart is not None:
        status = True

    
    videos = Videos.objects.filter(course_id=id).all()
    videos_count = Videos.objects.filter(course_id=id).count()
    Introduction_Video = IntroductionVideo.objects.filter(course_id=id).last()

    course = Courses.objects.filter(id=id).first()
    settings = SiteSettings.objects.last()
    title = settings.title + ' ' + '-' + ' ' + f'{course.CourseName}'
    context = {
        'title': title,
        'status': status,
        'videos': videos,
        'videos_count': videos_count,
        'keyWord': course.keyWord,
        'Introduction_Video': Introduction_Video,
        'course': course,
    }

    return render(request,'courses/showCourse_page/show_course.html',context)