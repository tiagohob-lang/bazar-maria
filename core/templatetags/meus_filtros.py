from django import template
import locale

register = template.Library()

@register.filter
def real_brasileiro(valor):
    try:
        # Formata com 2 casas decimais e troca o ponto pela vírgula
        return "{:,.2f}".format(float(valor)).replace(",", "X").replace(".", ",").replace("X", ".")
    except (ValueError, TypeError):
        return valor