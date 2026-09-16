# # apps/pages/templatetags/navigation_tags.py
# from django import template
# from django.urls import reverse, NoReverseMatch

# register = template.Library()

# @register.simple_tag(takes_context=True)
# def is_active(context, url_name, css_class='active'):
#     """
#     Mengembalikan nama class (default: 'active') jika URL yang diminta
#     cocok dengan URL halaman saat ini.
#     """
#     request = context.get('request')
#     if not request:
#         return ''
    
#     try:
#         # Cek jika path saat ini diawali atau sama dengan rute URL tujuan
#         if request.path == reverse(url_name):
#             return css_class
#     except NoReverseMatch:
#         pass
#     return ''


# apps/pages/templatetags/navigation_tags.py
from django import template
from django.urls import reverse, NoReverseMatch

register = template.Library()

@register.simple_tag(takes_context=True)
def is_active(context, url_name, css_class='active', exact=False):
    """
    Mengembalikan nama class jika URL halaman saat ini cocok.
    - exact=True : Jalur harus sama persis (cocok untuk Home).
    - exact=False: Selama jalur diawali oleh URL induk, akan dianggap aktif (cocok untuk Blog & Detail).
    """
    request = context.get('request')
    if not request:
        return ''
    
    try:
        target_url = reverse(url_name)
        current_path = request.path
        
        if exact:
            if current_path == target_url:
                return css_class
        else:
            # Memastikan sub-path seperti /blog/123/ tetap menyalakan menu /blog/
            if current_path.startswith(target_url) and target_url != '/':
                return css_class
            elif current_path == target_url:
                return css_class
                
    except NoReverseMatch:
        pass
    return ''
