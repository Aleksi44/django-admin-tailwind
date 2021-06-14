from django import template
from django_admin_tailwind import context

register = template.Library()


@register.filter
def get_context(key):
    return getattr(context, key, '')
