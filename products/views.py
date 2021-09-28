from django.shortcuts import render,redirect
from siteSettings.models import SiteSettings
from django.core.paginator import Paginator
from django.contrib import messages
from users.models import User
from .models import Product


def physicalProducts_page(request):
    if request.user.is_authenticated:
        if request.user.phone_authentication != True:
            return redirect('account:code_page')
        else:
            user_info = User.objects.filter(username=request.user.username).first()
            
            if user_info.block == True:
                messages.error(request, 'اکانت شما مسدود شده است لطفا با پشتیبانی تماس بگیرید')
                return redirect('contact:contactus_page')
    else: return redirect('account:login_page')

    products = Product.objects.filter(digital_or_physical=True,is_active=True).all()
    paginator = Paginator(products, 10)
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)
    settings = SiteSettings.objects.last()
    title = settings.title + ' ' + '-' + ' ' + 'محصولات فیزیکی'

    context = {
        'title': title,
        'prodcuts': page_obj,
    }

    return render(request,'product/physical_products/Physical_products.html',context)





def digitalProducts_page(request):
    if request.user.is_authenticated:
        if request.user.phone_authentication != True:
            return redirect('account:code_page')
        else:
            user_info = User.objects.filter(username=request.user.username).first()
            
            if user_info.block == True:
                messages.error(request, 'اکانت شما مسدود شده است لطفا با پشتیبانی تماس بگیرید')
                return redirect('contact:contactus_page')
    else: return redirect('account:login_page')

    products = Product.objects.filter(digital_or_physical=False,is_active=True).all()
    paginator = Paginator(products, 10)
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)
    settings = SiteSettings.objects.last()
    title = settings.title + ' ' + '-' + ' ' + 'محصولات دیجیتالی'

    context = {
        'title': title,
        'prodcuts': page_obj,
    }

    return render(request,'product/digital_products/Digital_products.html',context)


def productDisplay_page(request,slug):
    if request.user.is_authenticated:
        if request.user.phone_authentication != True:
            return redirect('account:code_page')
        else:
            user_info = User.objects.filter(username=request.user.username).first()
            
            if user_info.block == True:
                messages.error(request, 'اکانت شما مسدود شده است لطفا با پشتیبانی تماس بگیرید')
                return redirect('contact:contactus_page')
    else: return redirect('account:login_page')


    settings = SiteSettings.objects.last()
    product = Product.objects.filter(is_active=True,slug__iexact=slug).first()
    Latest_products = Product.objects.all().order_by('-id')[:3]
    if product is None:
        return redirect('home_page')
    else:
        title = settings.title + ' ' + '-' + ' ' + f'{product.title}'

        context = {
            'Latest_products': Latest_products,
            'product': product,
            'keyWord': product.keyWord,
            'title': title,

        }
        return render(request,'product/product_display/production-single.html',context)

