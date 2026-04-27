from django.urls import path
from carrinho import views

urlpatterns = [
    path('',views.visualizarCarrinho, name = 'carrinho'),
    path('adicionar_carrinho/<int:produto_id>', views.adicionarCarrinho, name='adicionarCarrinho'),
    path('diminuir_item_carrinho/<int:produto_id>', views.diminuirItemCarrinho, name='diminuirItemCarrinho'),
    path('remover_item_carrinho/<int:produto_id>', views.removerItemCarrinho, name='removerItemCarrinho')
]