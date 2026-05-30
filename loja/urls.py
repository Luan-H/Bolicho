from django.urls import path

from loja import views

urlpatterns = [
    path('', views.visualizarLoja, name='loja'),
    path('categoria/<slug:categoria_slug>/',views.visualizarLoja, name='produtos_por_categoria'),
    path('categoria/<slug:categoria_slug>/<slug:produto_slug>',views.visualizarDetalhesProduto ,name='produto_detalhe')
]