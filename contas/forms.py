from django import forms

from contas.models import Usuario

class FormularioRegistroUsuario(forms.ModelForm):
    
    senha = forms.CharField(widget = forms.PasswordInput(attrs={
        'placeholder' : 'Entre com a senha',
        'class' : 'form-control'
    }))
    confirmar_senha = forms.CharField(widget= forms.PasswordInput(attrs={
        'placeholder' : 'Confirme a senha',
        'class' : 'form-control'
    }))
    class Meta:
        model = Usuario
        fields = [ 'nome', 'nomeUsuario', 'email', 'telefone']

    def clean(self):
        cleaned_data = super(FormularioRegistroUsuario, self).clean()
        senha = cleaned_data.get('senha')
        confirmar_senha = cleaned_data.get('confirmar_senha')

        if senha != confirmar_senha:
            raise forms.ValidationError('as senhas não conferem')
        
        
    def __init__(self, *args, **kwargs):
        super(FormularioRegistroUsuario, self).__init__(*args, **kwargs)
        self.fields['nome'].widget.attrs['placeholder'] = 'Informe o nome'
        self.fields['nomeUsuario'].widget.attrs['placeholder'] = 'Informe o nome do usuario'
        self.fields['email'].widget.attrs['placeholder'] = 'Informe o e-mail'
        self.fields['telefone'].widget.attrs['placeholder'] = 'Informe o telefone'
        
        for field in self.fields:
            self.fields[field].widget.attrs['class'] = 'form-control'
