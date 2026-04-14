from django.shortcuts import render
from .models import Produto, Publico, TipoRoupa
from django.shortcuts import get_object_or_404

def vitrine(request):
    produtos = Produto.objects.filter(estoque__gt=0)
    
    # Pegamos os filtros da URL (ex: ?publico=1)
    publico_id = request.GET.get('publico')
    tipo_id = request.GET.get('tipo')

    if publico_id:
        produtos = produtos.filter(publico_id=publico_id)
    if tipo_id:
        produtos = produtos.filter(tipo_id=tipo_id)

    contexto = {
        'produtos': produtos,
        'publicos': Publico.objects.all(),
        'tipos': TipoRoupa.objects.all(),
    }
    return render(request, 'core/vitrine.html', contexto)

def detalhe_produto(request, pk):
    produto = get_object_or_404(Produto, pk=pk)
    return render(request, 'core/detalhe.html', {'produto': produto})