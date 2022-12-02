from django import template

from ..models import Menu , NavbarLogo , Footer

register = template.Library()


@register.simple_tag()
def get_menu(slug):
    return Menu.objects.filter(slug=slug).first()


@register.simple_tag()
def navbarlogo():
    return NavbarLogo.objects.first()

@register.simple_tag()
def footer():
    return Footer.objects.last()
