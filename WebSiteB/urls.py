from django.contrib import admin
from django.conf import settings
from django.urls import path,include
from django.conf.urls.static import static




urlpatterns = [
    path('',include('Home.urls')),
    path('ckeditor/', include('ckeditor_uploader.urls')),
    path('contact-us/', include('contactUs.urls')),
    path('admin/', admin.site.urls, name='admin'),
    path('products/', include('products.urls')),
    path('courses/', include('courses.urls')),
    path('news/', include('news.urls')),
    path('about-us/', include('aboutUs.urls')),
    path('dr-abbas-zahedi/', include('aboutMe.urls')),
    path('api/', include('api.urls')),
    path('account/',include('account.urls')),
    path('userPanel/',include('userPanel.urls')),
    path('payment/',include('payment.urls')),
    path('cart/', include('carts.urls')),
    path('blog/',include('blog.urls')),
]



handler404 = 'WebSiteB.views.NotFound'


if settings.DEBUG:
    urlpatterns += urlpatterns + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)


    urlpatterns += urlpatterns + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)