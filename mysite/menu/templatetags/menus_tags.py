from django import template

from ..models import Menu , NavbarLogo , Footer, MenuItem, FourDivSection
from home.models import Leaderboard
from django.template.response import TemplateResponse
from wagtail.core.models import Page, Site
register = template.Library()


@register.simple_tag()
def get_menu(slug):
    return Menu.objects.filter(slug=slug).first()


@register.simple_tag()
def navbarlogo():
    return NavbarLogo.objects.last()

@register.simple_tag()
def footer():
    return Footer.objects.last()

@register.simple_tag()
# @register.inclusion_tag('streams/student_profile.html')
def leaderboard():
    return Leaderboard.objects.all()
    
@register.simple_tag()
def cards():
    return FourDivSection.objects.all()

@register.simple_tag(takes_context=True)
def get_site_root(context):
    # This returns a core.Page. The main menu needs to have the site.root_page
    # defined else will return an object attribute error ('str' object has no
    # attribute 'get_children')
    
    if context['request'].get_full_path() == '/':
        return True
    else:
        return False
    


    
 

