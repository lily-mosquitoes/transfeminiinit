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

@register.simple_tag
def read_more_cta():
    return _('read_more_cta')

@register.simple_tag
def get_language_list():
    language_list = [
        {
            'code': 'fi',
            'name': 'suomi',
        },
        {
            'code': 'sv',
            'name': 'svenska',
        },
        {
            'code': 'en',
            'name': 'english',
        },
    ]
    return language_list

@register.simple_tag
def all_tags_filter():
    return _('all_tags_filter')

@register.simple_tag
def time_filter_all():
    return _('time_filter_all')

@register.simple_tag
def get_time_filters():
    time_filters = [
        _('time_filter_past_year'),
        _('time_filter_recent'),
    ]
    return time_filters

@register.simple_tag
def get_verbose_field_name(instance, field_name):
    return instance._meta.get_field(field_name).verbose_name.title()
