from django.http import HttpResponse
from django.shortcuts import get_object_or_404, render

from categoria.models import Categoria
from produto.models import Produto

def visualizarHome(request):
    produtos = Produto.objects.all().filter(esta_disponivel=True)
    lista_produto = {
        'produtos' : produtos
    }
    return render(request, 'home.html', lista_produto)

def visualizarLoja(request, categoria_slug = None):
    produto_quant = 0
    produtos = None
    if categoria_slug != None:
        categ = get_object_or_404(Categoria, slug = categoria_slug)
        produtos = Produto.objects.all().filter(categoria = categ)
    else:
        produtos = Produto.objects.all()
    produto_quant = produtos.count()
    contexto = {
        'produtos' : produtos,
        'produto_quant' : produto_quant,
    }
    return render(request, 'home.html', contexto)