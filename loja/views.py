from django.shortcuts import get_object_or_404, render
from produto.models import Produto
from categoria.models import Categoria

def visualizarLoja(request, categoria_slug = None):
    if categoria_slug != None:
        categ = get_object_or_404(Categoria, slug = categoria_slug)
        produtos = Produto.objects.all().filter(categoria = categ)
    else:
        produtos = Produto.objects.all()
    contexto = {
        'prods' : produtos
    }
    return render(request, 'home.html', contexto)

def visualizarDetalhesProduto(request, categoria_slug, produto_slug):
    produto = Produto.objects.get(categoria__slug = categoria_slug, slug = produto_slug)
    contexto = {
        'prod' : produto,
    }
    return render(request, 'loja/produto_detalhe.html', contexto)