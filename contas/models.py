from django.db import models
from django.contrib.auth.models import AbstractBaseUser, BaseUserManager
# Create your models here.
class GerenciamentoUsuario(BaseUserManager):
    def criar_usuario(self, nome, nomeUsuario, email, telefone, senha = None):
        if not email:
            raise ValueError('Usuário deve ter um endereço de email')
        if not nomeUsuario:
            raise ValueError('Nome do usuário é obrigatório')
        
        usuario = self.model(
            email = self.normalize_email(email),
            nomeUsuario = nomeUsuario,
            nome = nome,
            telefone = telefone
        )
        usuario.set_password(senha)
        usuario.save(using=self._db)
        return usuario
    
    def create_superuser(self, nome, nomeUsuario, email, telefone, senha = None):
        
        usuario = self.criar_usuario(
            email = self.normalize_email(email),
            nomeUsuario = nomeUsuario,
            nome = nome,
            telefone = telefone,
            senha = senha
        )
        usuario.is_admin = True
        usuario.is_staff = True
        usuario.is_superadmin = True
        
        return usuario
    
    
    
class Usuario(AbstractBaseUser):
    nome = models.CharField(max_length=100)
    nomeUsuario = models.CharField(max_length=80)
    email = models.EmailField(max_length=150, unique=True)
    telefone = models.CharField(max_length=15)
    is_admin = models.BooleanField(default=False)
    is_staff = models.BooleanField(default=False)
    is_active = models.BooleanField(default=True)
    is_superuser = models.BooleanField(default=False)
    
    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['nome', 'nomeUsuario']
    
    objects = GerenciamentoUsuario()