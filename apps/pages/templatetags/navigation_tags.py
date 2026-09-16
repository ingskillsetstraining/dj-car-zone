# apps/pages/templatetags/navigation_tags.py
from django import template
from django.urls import reverse, NoReverseMatch

register = template.Library()

@register.simple_tag(takes_context=True)
def is_active(context, url_name, css_class='active'):
    """
    Mengembalikan nama class (default: 'active') jika URL yang diminta
    cocok dengan URL halaman saat ini.
    """
    request = context.get('request')
    if not request:
        return ''
    
    try:
        # Cek jika path saat ini diawali atau sama dengan rute URL tujuan
        if request.path == reverse(url_name):
            return css_class
    except NoReverseMatch:
        pass
    return ''
