from django.shortcuts import render # Importa o renderizador de templates do Django
from rest_framework.generics import ListCreateAPIView, RetrieveUpdateDestroyAPIView # Para views baseadas em classes genéricas
from rest_framework.views import APIView # Para criar views baseadas em classes
from rest_framework.response import Response # Para respostas HTTP
from rest_framework import status # Para respostas HTTP
from .models import Imovel, Usuario, Contrato, Pagamento # Modelos importados
from .serializers import ImovelSerializer, UsuarioSerializer, ContratoSerializer, PagamentoSerializer # Serializers importados
from rest_framework.decorators import api_view # Decorador para views baseadas em funções
from .serializers import *
from rest_framework.viewsets import ModelViewSet
from rest_framework.permissions import IsAuthenticated
from django_filters.rest_framework import DjangoFilterBackend
from .filters import UsuarioFilter

############### Com NodelViewSet ########################

class UsuarioViewSet(ModelViewSet):
    queryset = Usuario.objects.all() 
    serializer_class = UsuarioSerializer
    # permission_classes = [IsAuthenticated] # Permissões para acesso a viewset (ex: IsAuthenticated, AllowAny, etc)

    filter_backends = [DjangoFilterBackend] # Configura o backend de filtragem
    filterset_class = UsuarioFilter # Especifica a classe de filtro para a viewset




    # def get_queryset(self):
    #     tipo = self.request.query_params.get('tipo', None) # Recebe o parâmetro 'tipo' da query string
    #     if tipo:
    #         self.queryset = self.queryset.filter(tipo=tipo) # Filtra os usuários pelo tipo, se o parâmetro for fornecido
    #     return self.queryset # Retorna o queryset filtrado ou completo, dependendo da presença do parâmetro 'tipo'

class ImovelViewSet(ModelViewSet):
    queryset = Imovel.objects.all()
    serializer_class = ImovelSerializer

    # def get_queryset(self):
    #     tipo= self.request.query_params.get('tipo', None) # Recebe o parâmetro 'tipo' da query string
    #     status= self.request.query_params.get('status', None) # Recebe o parâmetro 'status' da query string

    #     if tipo:
    #         self.queryset = self.queryset.filter(tipo=tipo) # Filtra os imóveis pelo tipo, se o parâmetro for fornecido
    #     if status:
    #         self.queryset = self.queryset.filter(status=status) # Filtra os imóveis pelo status, se o parâmetro for fornecido
    #     return self.queryset # Retorna o queryset filtrado ou completo, dependendo da presença dos parâmetros 'tipo' e 'status'

class ContratoViewSet(ModelViewSet):
    queryset = Contrato.objects.all()
    serializer_class = ContratoSerializer

class PagamentoViewSet(ModelViewSet):
    queryset = Pagamento.objects.all()
    serializer_class = PagamentoSerializer









# #############GET E POST USUARIO ####################
# @api_view(['GET', 'POST'])
# def listar_usuarios(request): # parametro de request (formulario), para receber os dados do request e retornar os dados do banco de dados
#      if request.method =='GET':
#           queryset = Usuario.objects.all() # consulta todos os usuarios
#           serializers = UsuarioSerializer(queryset, many=True) # serializa os dados (vários objetos)
#           return Response(serializers.data) # retorna os dados serializados
#      elif request.method == 'POST':
#           serializers= UsuarioSerializer(data = request.data) # Ele recebe os dados e transforma em djson
#           if serializers.is_valid(): # valida os dados
#                 serializers.save() # salva os dados no banco
#                 return Response(serializers.data, status=status.HTTP_201_CREATED) # retorna os dados salvos com status 201
#           else:
#                 return Response(serializers.errors, status=status.HTTP_400_BAD_REQUEST) # retorna os erros com status 400


# #############GET E POST USUARIO ####################
# class UsuarioListCreateAPIView(ListCreateAPIView): # classe para listar e criar usuarios
#     queryset = Usuario.objects.all()
#     serializer_class = UsuarioSerializer


# ############ UPDATE E DELETE USUARIO ##############
# class UsuarioDetailView(RetrieveUpdateDestroyAPIView): # classe para atualizar e deletar usuarios
#      queryset = Usuario.objects.all()
#      serializer_class = UsuarioSerializer



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
          
# ############ GET e POST Imovel ####################
# class ImovellistCreateAPIView(ListCreateAPIView):
#      queryset = Imovel.objects.all()
#      serializer_class = ImovelSerializer

# ############ UPDATE E DELETE IMOVEL ##############
# class ImovelDetailView(RetrieveUpdateDestroyAPIView):
#      queryset = Imovel.objects.all()
#      serializer_class = ImovelSerializer





# ############ GET e POST Contrato ####################
# @api_view(['GET', 'POST'])
# def listar_contratos(request):
#      if request.method == 'GET':
#           queryset = Contrato.objects.all()
#           serializers = ContratoSerializer(queryset, many=True)
#           return Response(serializers.data)
#      elif request.method == 'POST':
#           serializers = ContratoSerializer(data=request.data)
#           if serializers.is_valid():
#                 serializers.save()
#                 return Response(serializers.data, status=status.HTTP_201_CREATED)
#           else:
#                 return Response(serializers.errors, status=status.HTTP_400_BAD_REQUEST)
          
# ############ GET e POST Contrato ####################
# class ContratolistCreateAPIView(ListCreateAPIView):
#      queryset = Contrato.objects.all()
#      serializer_class = ContratoSerializer

# ############ UPDATE E DELETE CONTRATO ##############
# class ContratoDetailView(RetrieveUpdateDestroyAPIView):
#         queryset = Contrato.objects.all()
#         serializer_class = ContratoSerializer

    



# ############ GET e POST Pagamento ####################
# @api_view(['GET', 'POST'])
# def listar_pagamentos(request):
#     if request.method == 'GET':
#           queryset = Pagamento.objects.all()
#           serializers = PagamentoSerializer(queryset, many=True)
#           return Response(serializers.data)
#     elif request.method == 'POST':
#           serializers = PagamentoSerializer(data=request.data)
#           if serializers.is_valid():
#                 serializers.save()
#                 return Response(serializers.data, status=status.HTTP_201_CREATED)
#           else:
#                 return Response(serializers.errors, status=status.HTTP_400_BAD_REQUEST)

# ############ GET e POST Pagamento ####################
# class PagamentolistCreateAPIView(ListCreateAPIView):
#         queryset = Pagamento.objects.all()
#         serializer_class = PagamentoSerializer

# ############ UPDATE E DELETE PAGAMENTO ##############
# class PagamentoDetailView(RetrieveUpdateDestroyAPIView):
#         queryset = Pagamento.objects.all()
#         serializer_class = PagamentoSerializer #colocar mensagem de erro se nao achar o pagamento


# def get(self, request):
#       usuario = Usuario.objects.all()
#       serializer = UsuarioSerializer(usuario, many=True)
#       return Response(serializer.data)

# def post(self, request):
#       seriallizer = UsuarioSerializer(data=request.data)#recebe os dados do request e transforma em json
#       if seriallizer.is_valid(): #valida os dados
#             seriallizer.save() #salva os dados no banco
#             return Response(seriallizer.data, status=status.HTTP_201_CREATED) #retorna os dados salvos com status 201
#       return Response(seriallizer.errors, status=status.HTTP_400_BAD_REQUEST) #retorna os erros com status 400

# class ImovelListCreateAPIView(ListCreateAPIView):
#     queryset = Imovel.objects.all()
#     serializer_class = ImovelSerializer

# class ImovelDetailView(RetrieveUpdateDestroyAPIView):
#     queryset = Imovel.objects.all()
#     serializer_class = ImovelSerializer

# class PagamentoListCreateAPIView(ListCreateAPIView):
#     queryset = Pagamento.objects.all()
#     serializer_class = PagamentoSerializer

# class PagamentoDetailView(RetrieveUpdateDestroyAPIView):
#     queryset = Pagamento.objects.all()
#     serializer_class = PagamentoSerializer

# class ContratoListCreateAPIView(ListCreateAPIView):
#     queryset = Contrato.objects.all()
#     serializer_class = ContratoSerializer

# class ContratoDetailView(RetrieveUpdateDestroyAPIView):
#     queryset = Contrato.objects.all()
#     serializer_class = ContratoSerializer
    
# ############################## Via APIView ###########################################
# class UsuarioListCreateAPIView(APIView):

#     def get(self, request):
#         usuarios = Usuario.objects.all()
#         serializer = UsuarioSerializer(usuarios, many=True)
#         return Response(serializer.data)
    
#     def post(self, request):
#         serializer = UsuarioSerializer(data=request.data)
#         if serializer.is_valid():
#             serializer.save()
#             return Response(serializer.data, status=status.HTTP_201_CREATED)
#         return Response(serializer.data, status=status.HTTP_400_BAD_REQUEST)
    

# class UsuarioDetailView(APIView):

#     def get_object(self, pk):
#         return Usuario.objects.get(pk=pk)
    
#     def get(self, pk):
#         usuario =  self.get_object(pk)
#         serializer = UsuarioSerializer(usuario)
#         return Response(serializer.data)
    
#     def delete(self, request, pk ):
#         usuario = self.get_object(pk)
#         usuario.delete()
#         return Response(status=status.HTTP_204_NO_CONTENT)
    
#     def put(self, request, pk):
#         usuario = self.get_object(pk)
#         serializer = UsuarioSerializer(usuario, data = request.data)
#         if serializer.is_valid():
#             serializer.save()
#             return Response(serializer.data)
#         return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
      

# class ImovelListCreateAPIView(APIView):

#     def get(self, request):
#         Imovels = Imovel.objects.all()
#         serializer = ImovelSerializer(Imovels, many=True)
#         return Response(serializer.data)
    
#     def post(self, request):
#         serializer = ImovelSerializer(data=request.data)
#         if serializer.is_valid():
#             serializer.save()
#             return Response(serializer.data, status=status.HTTP_201_CREATED)
#         return Response(serializer.data, status=status.HTTP_400_BAD_REQUEST)
    

# class ImovelDetailView(APIView):

#     def get_object(self, pk):
#         return Imovel.objects.get(pk=pk)
    
#     def get(self, pk):
#         Imovel =  self.get_object(pk)
#         serializer = ImovelSerializer(Imovel)
#         return Response(serializer.data)
    
#     def delete(self, request, pk ):
#         Imovel = self.get_object(pk)
#         Imovel.delete()
#         return Response(status=status.HTTP_204_NO_CONTENT)
    
#     def put(self, request, pk):
#         Imovel = self.get_object(pk)
#         serializer = ImovelSerializer(Imovel, data = request.data)
#         if serializer.is_valid():
#             serializer.save()
#             return Response(serializer.data)
#         return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


# class PagamentoListCreateAPIView(APIView):

#     def get(self, request):
#         Pagamentos = Pagamento.objects.all()
#         serializer = PagamentoSerializer(Pagamentos, many=True)
#         return Response(serializer.data)
    
#     def post(self, request):
#         serializer = PagamentoSerializer(data=request.data)
#         if serializer.is_valid():
#             serializer.save()
#             return Response(serializer.data, status=status.HTTP_201_CREATED)
#         return Response(serializer.data, status=status.HTTP_400_BAD_REQUEST)
    

# class PagamentoDetailView(APIView):

#     def get_object(self, pk):
#         return Pagamento.objects.get(pk=pk)
    
#     def get(self, pk):
#         Pagamento =  self.get_object(pk)
#         serializer = PagamentoSerializer(Pagamento)
#         return Response(serializer.data)
    
#     def delete(self, request, pk ):
#         Pagamento = self.get_object(pk)
#         Pagamento.delete()
#         return Response(status=status.HTTP_204_NO_CONTENT)
    
#     def put(self, request, pk):
#         Pagamento = self.get_object(pk)
#         serializer = PagamentoSerializer(Pagamento, data = request.data)
#         if serializer.is_valid():
#             serializer.save()
#             return Response(serializer.data)
#         return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    


# class ContratoListCreateAPIView(APIView):

#     def get(self, request):
#         Contratos = Contrato.objects.all()
#         serializer = ContratoSerializer(Contratos, many=True)
#         return Response(serializer.data)
    
#     def post(self, request):
#         serializer = ContratoSerializer(data=request.data)
#         if serializer.is_valid():
#             serializer.save()
#             return Response(serializer.data, status=status.HTTP_201_CREATED)
#         return Response(serializer.data, status=status.HTTP_400_BAD_REQUEST)
    

# class ContratoDetailView(APIView):

#     def get_object(self, pk):
#         return Contrato.objects.get(pk=pk)
    
#     def get(self, pk):
#         Contrato =  self.get_object(pk)
#         serializer = ContratoSerializer(Contrato)
#         return Response(serializer.data)
    
#     def delete(self, request, pk ):
#         Contrato = self.get_object(pk)
#         Contrato.delete()
#         return Response(status=status.HTTP_204_NO_CONTENT)
    
#     def put(self, request, pk):
#         Contrato = self.get_object(pk)
#         serializer = ContratoSerializer(Contrato, data = request.data)
#         if serializer.is_valid():
#             serializer.save()
#             return Response(serializer.data)
#         return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)   
    





