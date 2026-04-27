from django.shortcuts import get_object_or_404, redirect, render
from django.core.exceptions import ObjectDoesNotExist

from carrinho.models import Carrinho, CarItem
from produto.models import Produto

from decimal import Decimal

def _getCarId(request):
    carSession = request.session.session_key
    if not carSession:
        carSession = request.session.create()
    return carSession

def adicionarCarrinho(request, produto_id):
    produto = Produto.objects.get(id=produto_id)
    try:
        carrinho = Carrinho.objects.get(car_id=_getCarId(request))
    except Carrinho.DoesNotExist:
        carrinho = Carrinho.objects.create(
            car_id = _getCarId(request)
        )
    carrinho.save()
    
    try:
        car_item = CarItem.objects.get(produto = produto, carrinho = carrinho)
        car_item.quantidade += 1
        car_item.preco = produto.preco
        car_item.save()
    except CarItem.DoesNotExist:
        car_item = CarItem.objects.create(
            produto = produto,
            quantidade = 1,
            carrinho = carrinho,
            preco = produto.preco
        )
        car_item.save()
    return redirect('carrinho')
        


def visualizarCarrinho(request, total=0, quantidade=0, car_items=None, total_geral =0):
    total_carrinho = 0
    imposto = 0
    taxa = 0.2
    valor_decimal = Decimal(str(taxa))
    try:
        carrinho = Carrinho.objects.get(car_id = _getCarId(request))
        car_items = CarItem.objects.filter(carrinho = carrinho)
        for car_item in car_items:
            total += (car_item.produto.preco * car_item.quantidade)
            quantidade += car_item.quantidade
            total_geral += total
        imposto = total_geral * valor_decimal
        total_carrinho = imposto + total_geral
    except ObjectDoesNotExist:
        pass
    
    contexto= {
        'total' : total,
        'quantidade' : quantidade,
        'car_items' : car_items,
        'total_geral' : total_geral,
        'total_carrinho' : round(total_carrinho, 2),
        'imposto' : round(imposto, 2)
    }
    return render(request, 'loja/carrinho.html', contexto)

def diminuirItemCarrinho(request, produto_id):
    carrinho = Carrinho.objects.get(car_id=_getCarId(request))
    produto = get_object_or_404(Produto, id = produto_id)
    car_item = CarItem.objects.get(produto = produto, carrinho = carrinho)
    
    if car_item.quantidade > 1:
        car_item.quantidade -= 1
        car_item.save()
    else:
        car_item.delete()
    return redirect('carrinho')

def removerItemCarrinho(request, produto_id):
    carrinho = Carrinho.objects.get(car_id=_getCarId(request))
    produto = get_object_or_404(Produto, id = produto_id)
    car_item = CarItem.objects.get(produto = produto, carrinho = carrinho)
    
    car_item.delete()
    return redirect('carrinho')