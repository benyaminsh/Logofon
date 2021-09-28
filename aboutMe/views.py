from siteSettings.models import SiteSettings
from django.shortcuts import render
from .models import AboutMe

def aboutDr(request):
    settings = SiteSettings.objects.last()
    aboutme = AboutMe.objects.last()
    context = {
        'settings': settings,
        'aboutMe': aboutme,
        'title': aboutme.name,
    }

    return render(request,'aboutDr/aboutDr.html',context)
