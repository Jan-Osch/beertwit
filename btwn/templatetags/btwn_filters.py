from django import template

from btwn.models import UserProfile

register = template.Library()


@register.filter(name='public_posts')
def public_post(posts):
    return [post for post in posts if post.public]


@register.filter(name='profile_name')
def profile_name(user):
    return UserProfile.objects.get(user=user).profile_name
