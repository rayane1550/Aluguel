from django.urls import path, include
from .views import *
from rest_framework.routers import DefaultRouter
from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
)



router = DefaultRouter()

router.register(r'usuarios', UsuarioViewSet, basename='usuario') # como é um ModelViewSet, o DRF já sabe que as URLs devem ser do tipo /usuarios/ e /usuarios/<id>/
router.register(r'imoveis', ImovelViewSet, basename='imovel')
router.register(r'contratos', ContratoViewSet, basename='contrato')
router.register(r'pagamentos', PagamentoViewSet, basename='pagamento')

urlpatterns = [

    path('token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('refresh/', TokenRefreshView.as_view(), name='token_refresh'),
    path('', include(router.urls)),
]

# from .views import *

# urlpatterns = [
#     path('usuarios/', UsuarioListCreateAPIView.as_view()),
#     path('usuario/<int:pk>/', UsuarioDetailView.as_view()), # Endpoint para update e delete de usuario


#     path('imoveis/', ImovelListCreateAPIView.as_view()),
#     path('imovel/<int:pk>/', ImovelDetailView.as_view()), # Endpoint para update e delete de imovel


#     path('contratos/', ContratoListCreateAPIView.as_view()),
#     path('contrato/<int:pk>/', ContratoDetailView.as_view()),
    
#     path('pagamentos/', PagamentoListCreateAPIView.as_view()),
#     path('pagamento/<int:pk>/', PagamentoDetailView.as_view()),
# ]