from siteSettings.models import SiteSettings
from django.core.paginator import Paginator
from django.shortcuts import render,redirect
from django.contrib.auth import logout
from django.contrib import messages
from comments.models import Comment
from users.models import User
from carts.models import *


def userPanel_page(request):
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
    comment_like = Comment.objects.filter(owner__username=request.user.username,status=True).count()
    course = Course.objects.filter(cart__owner__username=request.user.username,is_paid=True).count()
    print(course)
    digitalordering = Digital.objects.filter(cart__owner__username=request.user.username,is_paid=True).count()
    physicalproducts = Physical.objects.filter(cart__owner__username=request.user.username,is_paid=True).count()

    context = {
        'settings': settings,
        'comment_like': comment_like,
        'course': course,
        'digitalordering': digitalordering,
        'physicalproducts': physicalproducts,
    }
    return render(request,'userPanel/User_panel/User_panel.html',context)



def changePassword_page(request):
    if request.user.is_authenticated:
        if request.user.phone_authentication != True:
            return redirect('account:code_page')
        else:
            user_info = User.objects.filter(username=request.user.username).first()
            
            if user_info.block == True:
                messages.error(request, 'اکانت شما مسدود شده است لطفا با پشتیبانی تماس بگیرید')
                return redirect('contact:contactus_page')
    else: return redirect('account:login_page')


    if request.method == 'POST':
        password1 = request.POST['password1']
        password2 = request.POST['password2']


        if password1 == password2:
            check_password:User = User.objects.filter(username=request.user.username).first()
            check_password.set_password(password1)
            check_password.save()
            logout(request)
            messages.success(request, "گذرواژه شما با موفقیت تغییر کرد.")
            return redirect('userPanel:changePassword_page')

        else:
            messages.error(request, "گذرواژه هایه وارد شده یکسان نیستند")
            return redirect('userPanel:changePassword_page')

    else: return render(request,'userPanel/change_password/change_password.html')



def changeProfile_page(request):
    if request.user.is_authenticated:
        if request.user.phone_authentication != True:
            return redirect('account:code_page')
        else:
            user_info = User.objects.filter(username=request.user.username).first()
            
            if user_info.block == True:
                messages.error(request, 'اکانت شما مسدود شده است لطفا با پشتیبانی تماس بگیرید')
                return redirect('contact:contactus_page')
    else: return redirect('account:login_page')

    if request.method == "POST":
        image = request.FILES['image']

        if image:
            image_str = str(image)
            suffix = ['png','jpeg','jpg']
            image_spilt = image_str.split('.')
            if image_spilt[-1] in suffix:
                change_photo: User = User.objects.filter(username=request.user.username).first()
                change_photo.user_photo.delete()
                change_photo.user_photo = image
                change_photo.save()
                messages.success(request, 'تصویر پروفایل  تغییر کرد.')
                return redirect('userPanel:userPanel_page')
            else:
                messages.error(request,'پسوند فایل محاز نیست')
                return render(request, 'userPanel/change_profile/change_profile.html')

        else:
            messages.error(request, 'مقادیر وارد شده اشتباه است')

    else: return render(request,'userPanel/change_profile/change_profile.html')



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

    product = Digital.objects.filter(is_paid=True,cart__owner__username=request.user.username).all()
    paginator = Paginator(product, 10)

    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)
    context = {
        'products': page_obj,
    }
    return render(request,'userPanel/digital_products/digital_products.html',context)


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

    product = Physical.objects.filter(is_paid=True,cart__owner__username=request.user.username).all()
    paginator = Paginator(product, 10)
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)
    context = {
        'products': page_obj,
    }
    return render(request,'userPanel/physical_products/physical_products.html',context)


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


    course = Course.objects.filter(is_paid=True,cart__owner__username=request.user.username).all()
    paginator = Paginator(course, 10)

    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)
    context = {
        'courses': page_obj,
    }
    return render(request,'userPanel/courses/courses.html',context)



def approvedComments_page(request):
    if request.user.is_authenticated:
        if request.user.phone_authentication != True:
            return redirect('account:code_page')
        else:
            user_info = User.objects.filter(username=request.user.username).first()
            
            if user_info.block == True:
                messages.error(request, 'اکانت شما مسدود شده است لطفا با پشتیبانی تماس بگیرید')
                return redirect('contact:contactus_page')
    else: return redirect('account:login_page')

    comments = Comment.objects.filter(owner__username=request.user.username,status=True).all()
    paginator = Paginator(comments, 10)

    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)

    context = {
        'comments': page_obj,
    }

    return render(request,'userPanel/approved_comments/approvedComments.html',context)


def unapprovedComments_page(request):
    if request.user.is_authenticated:
        if request.user.phone_authentication != True:
            return redirect('account:code_page')
        else:
            user_info = User.objects.filter(username=request.user.username).first()
            
            if user_info.block == True:
                messages.error(request, 'اکانت شما مسدود شده است لطفا با پشتیبانی تماس بگیرید')
                return redirect('contact:contactus_page')
    else: return redirect('account:login_page')

    comments = Comment.objects.filter(owner__username=request.user.username,status=False).all()
    paginator = Paginator(comments, 10)

    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)

    context = {
        'comments': page_obj,
    }

    return render(request,'userPanel/unapproved_comments/unapprovedComments.html',context)