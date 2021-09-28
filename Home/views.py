from siteSettings.models import SiteSettings
from django.shortcuts import render,redirect
from django.contrib import messages
from products.models import Product
from courses.models import Courses
from users.models import User
from blog.models import Blog


def home_page(request):
    if request.user.is_authenticated:
        if request.user.phone_authentication != True:
            return redirect('account:code_page')
        else:
            user_info = User.objects.filter(username=request.user.username).first()
            
            if user_info.block == True:
                messages.error(request, 'اکانت شما مسدود شده است لطفا با پشتیبانی تماس بگیرید')
                return redirect('contact:contactus_page')

    
    Physical_count = Product.objects.filter(digital_or_physical=False).count()
    Digital_count = Product.objects.filter(digital_or_physical=True).count()
    courses_count = Courses.objects.count()
    blog_count = Blog.objects.count()
    settings = SiteSettings.objects.last()
    courses = Courses.objects.order_by('-id').all()[:3]


    context = {
        'Physical_count': Physical_count,
        'Digital_count': Digital_count,
        'courses_count': courses_count,
        'blog_count': blog_count,
        'courses': courses,
        'settings': settings,
    }



    return render(request,'home_page/home.html',context)



