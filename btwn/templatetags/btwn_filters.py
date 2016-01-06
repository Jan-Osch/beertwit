from django import template

from btwn.models import UserProfile
from btwn.views import check_if_is_author

register = template.Library()


@register.filter(name='public_posts')
def public_post(posts):
    return [post for post in posts if post.public]


@register.filter(name='profile_name')
def profile_name(user):
    return UserProfile.objects.get(user=user).profile_name


@register.filter(name='is_author')
def is_author(user, instance):
    return check_if_is_author(user, instance)
