from django.shortcuts import render,redirect
from siteSettings.models import SiteSettings
from django.contrib import messages
from users.models import User
from .models import *

def news_page(request):
    if request.user.is_authenticated:
        if request.user.phone_authentication != True:
            return redirect('account:code_page')
        else:
            user_info = User.objects.filter(username=request.user.username).first()
            
            if user_info.block == True:
                messages.error(request, 'اکانت شما مسدود شده است لطفا با پشتیبانی تماس بگیرید')
                return redirect('contact:contactus_page')
    else: return redirect('account:login_page')

    news = News.objects.order_by('-id').all()
    settings = SiteSettings.objects.last()
    title = settings.title + ' ' + '-' + ' ' + 'اخبار'

    context = {
        'news': news,
        'title': title,

    }

    return render(request,'news/news_page/news_page.html',context)
