from django.urls import path
from contas import views


urlpatterns = [
    path('registrar/', views.registrarUsuario, name = 'registrar')
]