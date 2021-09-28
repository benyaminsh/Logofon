from siteSettings.models import SiteSettings
from django.contrib import messages
from django.shortcuts import render
from .forms import ContactForm
from .models import ContactUs

def contactus_page(request):
    settings = SiteSettings.objects.last()
    title = settings.title + ' ' + '-' + ' ' + 'تماس با ما'
    context = {
        'settings': settings,
        'title': title,
    }

    if request.method == "POST":
        name = request.POST['name']
        email = request.POST['email']
        subject = request.POST['subject']
        message = request.POST['message']

        if len(name) != 0:
            if len(email) != 0:
                if len(subject) != 0:
                    if len(message) != 0:
                        contactus = ContactUs.objects.create(name=name,email=email,subject=subject,message=message,status=False)
                        messages.success(request,'درخواست تماس ارسال شد')
                        return render(request, 'contactUs/contact.html', context)
                    else:
                        messages.error(request, 'لطفا پیام خود  را وارد کنید')
                        return render(request, 'contactUs/contact.html', context)

                else:
                    messages.error(request, 'لطفا عنوان تماس  را وارد کنید')
                    return render(request, 'contactUs/contact.html', context)

            else:
                messages.error(request, 'لطفا ایمیل خود را وارد کنید')
                return render(request, 'contactUs/contact.html', context)

        else:
            messages.error(request,'لطفا نام خود را وارد کنید')
            return render(request, 'contactUs/contact.html', context)

    else:
        return render(request, 'contactUs/contact.html', context)
