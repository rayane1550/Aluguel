from django.shortcuts import render # Importa o renderizador de templates do Django
from rest_framework.generics import ListCreateAPIView, RetrieveUpdateDestroyAPIView # Para views baseadas em classes genéricas
from rest_framework.views import APIView # Para criar views baseadas em classes
from rest_framework.response import Response # Para respostas HTTP
from rest_framework import status # Para respostas HTTP
from .models import Imovel, Usuario, Contrato, Pagamento # Modelos importados
from .serializers import ImovelSerializer, UsuarioSerializer, ContratoSerializer, PagamentoSerializer # Serializers importados
from rest_framework.decorators import api_view # Decorador para views baseadas em funções



#############GET E POST USUARIO ####################
@api_view(['GET', 'POST'])
def listar_usuarios(request): # parametro de request 
     if request.method =='GET':
          queryset = Usuario.objects.all() # consulta todos os usuarios
          serializers = UsuarioSerializer(queryset, many=True) # serializa os dados (vários objetos)
          return Response(serializers.data) # retorna os dados serializados
     elif request.method == 'POST':
          serializers= UsuarioSerializer(data = request.data) # Ele recebe os dados e transforma em djson
          if serializers.is_valid(): # valida os dados
                serializers.save() # salva os dados no banco
                return Response(serializers.data, status=status.HTTP_201_CREATED) # retorna os dados salvos com status 201
          else:
                return Response(serializers.errors, status=status.HTTP_400_BAD_REQUEST) # retorna os erros com status 400


#############GET E POST USUARIO ####################
class UsuarioListCreateAPIView(ListCreateAPIView): # classe para listar e criar usuarios
    queryset = Usuario.objects.all()
    serializer_class = UsuarioSerializer


############ UPDATE E DELETE USUARIO ##############
class UsuarioUpdateDestroyView(RetrieveUpdateDestroyAPIView): # classe para atualizar e deletar usuarios
     queryset = Usuario.objects.all()
     serializer_class = UsuarioSerializer





############ GET e POST Imovel ####################
@api_view(['GET', 'POST'])
def listar_imoveis(request):
     if request.method == 'GET':
          queryset = Imovel.objects.all()
          serializers = ImovelSerializer(queryset, many=True)
          return Response(serializers.data)
     elif request.method == 'POST':
          serializers = ImovelSerializer(data=request.data)
          if serializers.is_valid():
                serializers.save()
                return Response(serializers.data, status=status.HTTP_201_CREATED)
          else:
                return Response(serializers.errors, status=status.HTTP_400_BAD_REQUEST)
          
############ GET e POST Imovel ####################
class ImovellistCreateAPIView(ListCreateAPIView):
     queryset = Imovel.objects.all()
     serializer_class = ImovelSerializer

############ UPDATE E DELETE IMOVEL ##############
class ImovelUpdateDestroyView(RetrieveUpdateDestroyAPIView):
     queryset = Imovel.objects.all()
     serializer_class = ImovelSerializer





############ GET e POST Contrato ####################
@api_view(['GET', 'POST'])
def listar_contratos(request):
     if request.method == 'GET':
          queryset = Contrato.objects.all()
          serializers = ContratoSerializer(queryset, many=True)
          return Response(serializers.data)
     elif request.method == 'POST':
          serializers = ContratoSerializer(data=request.data)
          if serializers.is_valid():
                serializers.save()
                return Response(serializers.data, status=status.HTTP_201_CREATED)
          else:
                return Response(serializers.errors, status=status.HTTP_400_BAD_REQUEST)
          
############ GET e POST Contrato ####################
class ContratolistCreateAPIView(ListCreateAPIView):
     queryset = Contrato.objects.all()
     serializer_class = ContratoSerializer

############ UPDATE E DELETE CONTRATO ##############
class ContratoUpdateDestroyView(RetrieveUpdateDestroyAPIView):
        queryset = Contrato.objects.all()
        serializer_class = ContratoSerializer

    



############ GET e POST Pagamento ####################
@api_view(['GET', 'POST'])
def listar_pagamentos(request):
    if request.method == 'GET':
          queryset = Pagamento.objects.all()
          serializers = PagamentoSerializer(queryset, many=True)
          return Response(serializers.data)
    elif request.method == 'POST':
          serializers = PagamentoSerializer(data=request.data)
          if serializers.is_valid():
                serializers.save()
                return Response(serializers.data, status=status.HTTP_201_CREATED)
          else:
                return Response(serializers.errors, status=status.HTTP_400_BAD_REQUEST)

############ GET e POST Pagamento ####################
class PagamentolistCreateAPIView(ListCreateAPIView):
        queryset = Pagamento.objects.all()
        serializer_class = PagamentoSerializer

############ UPDATE E DELETE PAGAMENTO ##############
class PagamentoUpdateDestroyView(RetrieveUpdateDestroyAPIView):
        queryset = Pagamento.objects.all()
        serializer_class = PagamentoSerializer

