from django.shortcuts import redirect, render

from contas.models import Usuario
from contas.forms import FormularioRegistroUsuario

# Create your views here.
def registrarUsuario(request):
    if request.method == 'POST':
        form = FormularioRegistroUsuario(request.POST)
        if form.is_valid():
            nome = form.cleaned_data['nome']
            email = form.cleaned_data['email']
            telefone = form.cleaned_data['telefone']
            nomeUsuario = form.cleaned_data['nonomeUsuario']
            senha = form.cleaned_data['senha']

            usuario = Usuario.objects.criar_usuario(nome = nome, email = email, nomeUsuario = nomeUsuario, telefone = telefone, senha = senha)
            usuario.save()
            
            return redirect('login')
        
    else:
        formulario = FormularioRegistroUsuario
        
    contexto = {
        'form' : formulario
    }
    return render(request, 'contas/registrar.html', contexto)