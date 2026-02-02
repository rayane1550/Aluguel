from django.shortcuts import render
from rest_framework.generics import ListCreateAPIView
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .models import Imovel, Usuario, Contrato, Pagamento
from .serializers import ImovelSerializer, UsuarioSerializer, ContratoSerializer, PagamentoSerializer

# class UsuarioListCreateAPIView(APIView):
#     def get(self, request):
#         usuarios = Usuario.objects.all()
#         serializer = UsuarioSerializer(usuarios, many=True)
#         return Response(serializer.data)

#     def post(self, request):
#         serializer = UsuarioSerializer(data=request.data)


class UsuarioListCreateAPIView(ListCreateAPIView):
    queryset = Usuario.objects.all()
    serializer_class = UsuarioSerializer
