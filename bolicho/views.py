from django.http import HttpResponse
from django.shortcuts import render

from produto.models import Produto

def visualizarHome(request):
    produtos = Produto.objects.all().filter(esta_disponivel=True)
    lista_produto = {
        'produtos' : produtos
    }
    return render(request, 'home.html', lista_produto)