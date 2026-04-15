from django.db import models
from django.urls import reverse

from categoria.models import Categoria

# Create your models here.
class Produto(models.Model):
    nome = models.CharField(max_length=100, unique=True)
    descricao = models.TextField(max_length=255, unique=True)
    preco = models.DecimalField(max_digits=12, decimal_places=2)
    imagem = models.ImageField(upload_to='fotos/produtos/', blank=True)
    estoque = models.IntegerField()
    esta_disponivel = models.BooleanField(default=True)
    slug = models.SlugField(max_length=110, unique=True)
    criado_em = models.DateTimeField(auto_now_add=True)
    modificado_em = models.DateTimeField(auto_now=True)
    categoria = models.ForeignKey(Categoria, on_delete=models.CASCADE)
    def __str__(self):
        return self.nome
    
    def get_url(self):
        return reverse('produto_detalhe', args=[self.categoria.slug, self.slug])
    