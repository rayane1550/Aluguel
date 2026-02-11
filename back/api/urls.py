from django.urls import path
from .views import *

urlpatterns = [
    path('usuarios/', UsuarioListCreateAPIView.as_view()),
    path('usuario/<int:pk>/', UsuarioDetailView.as_view()), # Endpoint para update e delete de usuario


    path('imoveis/', ImovellistCreateAPIView.as_view()),
    path('imovel/<int:pk>/', ImovelDetailView.as_view()), # Endpoint para update e delete de imovel


    path('contratos/', ContratolistCreateAPIView.as_view()),
    path('contrato/<int:pk>/', ContratoDetailView.as_view()),
    
    path('pagamentos/', PagamentolistCreateAPIView.as_view()),
    path('pagamentos/<int:pk>/', PagamentoDetailView.as_view()),
]