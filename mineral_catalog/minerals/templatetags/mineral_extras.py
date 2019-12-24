from django import template

import markdown2
from django.utils.safestring import mark_safe

register = template.Library()

@register.filter('image_address')
def image_address(mineral):
    """ get the image address for html src """
    return "images/" + mineral.image_filename

@register.filter('markdown_to_html')
def markdown_to_html(markdown_text):
    """ conver markdown text to html """
    html_body = markdown2.markdown(markdown_text)
    return mark_safe(html_body)
