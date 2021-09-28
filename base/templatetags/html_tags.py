from django import template
from siteSettings.models import SiteSettings
from blog.models import Blog
from carts.models import *

register = template.Library()

@register.simple_tag()
def Logo():
    settings = SiteSettings.objects.last()

    return settings.Logo


@register.simple_tag()
def title():
    settings = SiteSettings.objects.last()

    return settings.name

@register.simple_tag()
def settings():
    settings = SiteSettings.objects.last()

    return settings

@register.simple_tag()
def blogs():
    blogs = Blog.objects.order_by('-id').all()[:3]

    return blogs



