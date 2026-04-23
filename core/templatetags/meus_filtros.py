from django import template
from django.utils import timezone
from datetime import timedelta

register = template.Library()

@register.filter
def real_brasileiro(valor):
    try:
        # Formata com 2 casas decimais e troca o ponto pela vírgula
        return "{:,.2f}".format(float(valor)).replace(",", "X").replace(".", ",").replace("X", ".")
    except (ValueError, TypeError):
        return valor

# ADICIONADO O DECORADOR ABAIXO PARA CORRIGIR O ERRO 500
@register.filter(name='eh_novo')
def eh_novo(data):
    if not data:
        return False
    # Define o limite de 48 horas atrás
    limite = timezone.now() - timedelta(hours=48)
    return data > limite