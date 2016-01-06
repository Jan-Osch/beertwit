from django import template

from btwn.views import check_if_is_author

register = template.Library()


@register.simple_tag(name='is_author')
def is_author(user, instance):
    return check_if_is_author(user, instance)
