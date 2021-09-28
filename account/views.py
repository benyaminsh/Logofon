from django.shortcuts import render,redirect
from django.contrib.auth import authenticate,login,logout
from siteSettings.models import SiteSettings
from django.contrib import messages
from users.models import User
from random import randint
from requests import post
from .models import Code




def account_page(request):
    if not request.user.is_authenticated:
        return redirect('account:login_page')
    else: return redirect('userPanel:userPanel_page')




def register_page(request):
    settings = SiteSettings.objects.last()
    context = {
        'title': f' ثبت نام - {settings.title}',
    }

    if request.user.is_authenticated:
        return redirect("account:account_page")

    if not request.session.session_key:
        request.session.save()

    if request.method == "POST":
        firstName_and_lastName = request.POST['firstName_and_lastName']



        phone = request.POST['phone']
        username = str(request.POST['username']).lower()
        password1 = request.POST['password1']
        password2 = request.POST['password2']

        try:
            Terms_and_Conditions = request.POST['Terms_and_Conditions']
        except:
            messages.error(request,'قوانین و شرایط را باید قبول کنید')
            return render(request, 'account/register_page/register.html', context)

        Letters = ['ظ', 'ط', 'ز', 'ر', 'ذ', 'د', 'ئ', 'و', 'م', 'ن', 'ت', 'ا', 'ل', 'ب', 'ک', 'گ', 'ب', 'ی', 'س', 'ش',
                   'ض', 'ص', 'ث', 'ق', 'ف', 'غ', 'ع', 'ه', 'خ', 'ح', 'ج', 'چ', 'پ', 'ژ', ' ']
        error = 0

        for ue in username:
            if ue in Letters:
                print(ue)
                error += 1

        if error > 0:
            messages.error(request, "لطفا داخل  یوزرنیم از حروف فارسی استفاده نکنید")
        else:
            if len(firstName_and_lastName) > 0:
                phone_check = User.objects.filter(phone=phone).first()
                if phone_check is None:
                    if len(phone) == 11:
                        username_check = User.objects.filter(username=username).first()
                        if username_check is None:
                            if password1 == password2:
                                create = User.objects.create(username=username,phone=phone,first_name=firstName_and_lastName,password=password1)
                                login(request,create)
                                messages.success(request,'حساب کاربری شما با موفقیت ایجاد شد')
                                return redirect('userPanel:userPanel_page')

                            else:
                                messages.error(request,'گذرواژه ها یک سان نیستند')
                                return render(request, 'account/register_page/register.html', context)

                        else:
                            messages.error(request,'کاربری با این یوزرنیم ثبت نام کرده است')
                            return render(request, 'account/register_page/register.html', context)
                    else:
                        messages.error(request, 'شماره تلفن را صحیح وارد کنید! مثال 09121404213')
                        return render(request, 'account/register_page/register.html', context)

                else:
                    messages.error(request,'کاربری با این شماره تلفن ثبت نام کرده است')
                    return render(request, 'account/register_page/register.html', context)

            else:
                messages.error(request,'لطفا نام و نام خانوداگی خود را وارد کنید')
                return render(request, 'account/register_page/register.html', context)

    return render(request, 'account/register_page/register.html', context)





def logout_page(request):
    if request.user.is_authenticated:
        logout(request)
        return redirect('account:login_page')

    else:
        return redirect('account:login_page')



def login_page(request):
    settings = SiteSettings.objects.last()
    if request.user.is_authenticated:
        return redirect('account:account_page')

    if not request.session.session_key:
        request.session.save()


    if request.method == "POST":
        username = request.POST['username']
        password = request.POST['password']
        user_check = User.objects.filter(username__iexact=username).first()

        if user_check:
            user_pass = authenticate(request, username=username, password=password)
            if user_pass:
                login(request, user_pass)
                messages.success(request, "با موفقیت وارد شدید")
                return redirect('userPanel:userPanel_page')
            else:
                messages.error(request, "مقادیر ورودی اشتباه است")
        else:
            messages.error(request, "کاربری با این مشخصات یافت نشد")


    context = {
        'title': f' ورود  - {settings.title}',
    }

    return render(request, 'account/login_page/login.html', context)



def code_page(request):

    if request.user.is_authenticated:
        user_info:User = User.objects.filter(username__iexact=request.user.username).first()
        if user_info.phone_authentication == True:
            return redirect('home_page')


    settings = SiteSettings.objects.last()
    context = {
        'title': f' فعالسازی حساب  - {settings.title}',
    }
    if request.method == "POST":
        code = request.POST['code']
        code_check = Code.objects.filter(code=code).first()
        if code_check is not None:
            code_check.status = True
            code_check.save()
            user = User.objects.filter(username=request.user.username).first()
            user.phone_authentication = True
            user.save()
            code_delete_Falses = Code.objects.filter(phone=user.phone,status=False).all()
            code_delete_Falses.delete()
            messages.success(request,'حساب شما فعال شد')
            return redirect('userPanel:userPanel_page')
        else:
            messages.error(request,'کده تایید اشتباه است')
            return render(request, 'account/code_page/getCode.html', context)
    else:
        user_info = User.objects.filter(username=request.user.username).first()
        code_count = Code.objects.filter(phone=user_info.phone,status=False).count()
        if code_count > 10:
            messages.error(request,'شما بیش از حد تلاش کردید لطفا با پشتیبانی تماس بگیرید')
            return render(request, 'account/code_page/getCode.html', context)
        else:
            code = randint(1, 100000)
            result = post(f'{settings.address_sms}',{'message': f'کده تایید شما : {code}','from': f'{settings.number_sms}','to': f'{user_info.phone}','UserName': f'{settings.username_sms}','Password': f'{settings.password_sms}'})
            code_create = Code.objects.create(code=code, phone=user_info.phone, status=False)
            return render(request, 'account/code_page/getCode.html', context)










def passwordReset_page(request):
    if request.user.is_authenticated:
        return redirect('home_page')

    settings = SiteSettings.objects.last()



    if request.method == 'POST':
        try:
            phone = request.POST['phone']
            phone_check = User.objects.filter(phone=phone).first()
            if phone_check is not None:
                code = randint(1, 100000)
                result = post(f'{settings.address_sms}',{'message': f'کده تایید شما : {code}','from': f'{settings.number_sms}','to': f'{phone}','UserName': f'{settings.username_sms}','Password': f'{settings.password_sms}'})
                code_create = Code.objects.create(code=code, phone=phone, status=False)
                messages.success(request,'کده تایید جهت تغییر پسورد به شماره تلفن شما ارسال شد')
                context = {
                    'title': f' حساب کاربری  - {settings.title}',
                    'form': True,
                }
                return render(request, 'account/passwordReset_page/passwordRest.html', context)
            else:
                messages.success(request,'کاربری با این مشخصات وجود ندارد')
                return redirect('account:login_page')
        except:
            code = request.POST['code']
            password1 = request.POST['password1']
            password2 = request.POST['password2']
            code_check = Code.objects.filter(code=code).first()
            if code_check is not None:
                if password1 == password2:
                    change_password = User.objects.filter(phone=code_check.phone).first()
                    change_password.set_password(password1)
                    change_password.save()
                    messages.success(request, 'گذرواژه با موفقیت تغییر کرد')
                    return redirect('userPanel:userPanel_page')

                else:
                    messages.error(request, 'گذرواژه ها یک سان نیستند')
                    context = {
                        'title': f' حساب کاربری  - {settings.title}',
                        'form': True,
                    }
                    return render(request, 'account/passwordReset_page/passwordRest.html', context)

            else:
                messages.error(request, 'کده تایید اشتباه است')
                context = {
                    'title': f' حساب کاربری  - {settings.title}',
                    'form': True,
                }
                return render(request, 'account/passwordReset_page/passwordRest.html', context)

    else:
        context = {
            'title': f' حساب کاربری  - {settings.title}',
        }
        return render(request, 'account/passwordReset_page/passwordRest.html', context)



