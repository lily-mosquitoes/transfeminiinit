from django import template
from django.utils.translation import gettext_lazy as _

register = template.Library()

@register.simple_tag
def title():
    return _('title')

@register.simple_tag
def info():
    return _('info')

@register.simple_tag
def membership():
    return _('membership')

@register.simple_tag
def contact():
    return _('contact')
