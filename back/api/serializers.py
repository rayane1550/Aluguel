from rest_framework import serializers
from .models import Imovel, Usuario, Contrato, Pagamento

class UsuarioSerializer(serializers.ModelSerializer): # voce esta dando a ele a capacidade de serializar usar o crud
    class Meta:
        model = Usuario
        fields = '__all__'  # inclui todos os campos do modelo Usuario

class ImovelSerializer(serializers.ModelSerializer):
    class Meta:
        model = Imovel
        fields = '__all__'  # inclui todos os campos do modelo Imovel

class ContratoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Contrato
        fields = '__all__'  # inclui todos os campos do modelo Contrato

class PagamentoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Pagamento
        fields = '__all__' 