
from django import template

from django.template.response import TemplateResponse

from django.template.defaultfilters import stringfilter

from wagtailmenus.models import FlatMenu
register = template.Library()

@register.simple_tag
def footer_menus():
    return FlatMenu.objects.filter(handle__endswith='footer')