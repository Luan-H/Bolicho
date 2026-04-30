from carrinho.models import CarItem, Carrinho
from carrinho.views import _getCarId


def obterContador(request):
    cont = 0
    itens = 0
    try:
        car = Carrinho.objects.get(car_id = _getCarId(request))
        carItens = CarItem.objects.all().filter(carrinho = car)
        ## assim se pega a quantidade de itens no carrinho
        itens = len(carItens)
        ## assim se pega a quantidade de itens dentro dos itens
        for item in carItens:
            cont += item.quantidade
    except Carrinho.DoesNotExist:
        cont = 0
        itens = 0
        
    return dict(car_cont = itens)