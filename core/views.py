from django.shortcuts import render, get_object_or_404
from .models import Produto, Publico, TipoRoupa

def vitrine(request):
    # 'tipo' e 'publico' são os nomes que aparecem na URL: ?tipo=1&publico=2
    tipo_id = request.GET.get('tipo')
    publico_id = request.GET.get('publico')

    produtos = Produto.objects.all()

    # No filter, usamos o nome do campo no seu Model Produto (tipo e publico)
    if tipo_id:
        produtos = produtos.filter(tipo_id=tipo_id)
    
    if publico_id:
        produtos = produtos.filter(publico_id=publico_id)

    # Buscamos as listas completas para os botões
    tipos_roupa = TipoRoupa.objects.all() 
    publicos = Publico.objects.all()

    return render(request, 'core/vitrine.html', {
        'produtos': produtos,
        'tipos_roupa': tipos_roupa, # Nome claro para o template
        'publicos': publicos
    })

def detalhe_produto(request, pk):
    produto = get_object_or_404(Produto, pk=pk)
    return render(request, 'core/detalhe.html', {'produto': produto})