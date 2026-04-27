from django.db import models
from produto.models import Produto
class Carrinho(models.Model):
    car_id = models.CharField(max_length=20, blank=True)
    data_criado = models.DateField(auto_now_add=True)
    data_modificado = models.DateField(auto_now=True)
    
    def __str__(self):
        return self.car_id
    
    
class CarItem(models.Model):
    produto = models.ForeignKey(Produto, on_delete=models.PROTECT)
    carrinho = models.ForeignKey(Carrinho, on_delete=models.CASCADE)
    quantidade = models.IntegerField()
    preco = models.DecimalField(decimal_places=2, max_digits=11)
    
    def sub_total(self):
        return self.produto.preco * self.quantidade
    
