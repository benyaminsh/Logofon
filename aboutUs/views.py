from siteSettings.models import SiteSettings
from django.shortcuts import render
from .models import AboutUs

def aboutus_page(request):
    settings = SiteSettings.objects.last()

    aboutus = AboutUs.objects.last()
    title = settings.title + ' ' + '-' + ' ' + 'درباره ما'
    context = {
        'title': title,
        'aboutus': aboutus,
    }
    return render(request, 'aboutUs/about.html', context)