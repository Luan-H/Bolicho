from categoria.models import Categoria


def listarMenuCategoria(request):
    categorias = Categoria.objects.all()
    return dict(listaCategorias = categorias)