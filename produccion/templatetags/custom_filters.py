# templatetags/custom_filters.py
from django import template

register = template.Library()

@register.filter
def get_item(dictionary, key):
    """Retorna el valor correspondiente a la clave del diccionario."""
    return dictionary.get(key)
