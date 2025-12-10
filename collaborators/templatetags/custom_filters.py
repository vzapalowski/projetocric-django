from django import template
register = template.Library()

@register.filter
def contains(value, text):
    """Retorna True se 'text' estiver dentro de 'value'."""
    if not value:
        return False
    return text.lower() in value.lower()