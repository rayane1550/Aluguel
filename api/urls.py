from django.urls import path
from .views import *

urlpatterns = [
    path('usuarios', UsuarioListCreateAPIView.as_view()),
    path('usuario/<int:pk>', UsuarioUpdateDestroyView.as_view()), # Endpoint para update e delete de usuario
    path('users', listar_usuarios), # Metodo para listar e criar usuarios
    path('imoveis', ImovellistCreateAPIView.as_view()),
    path('imovel/<int:pk>', ImovelUpdateDestroyView.as_view()), # Endpoint para update e delete de imovel
    path('imoveis_listar', listar_imoveis), # Metodo para listar e criar imoveis
    path('contratos', ContratolistCreateAPIView.as_view()),
    path('contrato/<int:pk>', ContratoUpdateDestroyView.as_view()),
    path('contratos_listar', listar_contratos), 
    path('pagamentos', PagamentolistCreateAPIView.as_view()),
    path('pagamentos/<int:pk>', PagamentoUpdateDestroyView.as_view()),
    path('pagamentos_listar', listar_pagamentos),
]