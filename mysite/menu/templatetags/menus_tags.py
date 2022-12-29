from django import template

from ..models import Menu , NavbarLogo , Footer, MenuItem
from home.models import Leaderboard
from django.template.response import TemplateResponse
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
    
