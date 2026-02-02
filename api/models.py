from django.db import models



class Usuario (models.Model): # ainda não está criado, tem que dar mikemigrate para criar a tabela no banco
    TIPO_CHOICES = [
        ('LOCADOR', 'locador'),
        ('LOCATARIO', 'locatario')
    ]

    nome = models.CharField(max_length=100)
    email = models.EmailField()
    telefone = models.CharField(max_length=20, blank=True, null=True)
    tipo = models.CharField(choices=TIPO_CHOICES)
    
    def __str__(self):
        return self.nome 


class Imovel (models.Model): # class usuario
    STATUS_CHOICES = [
        ('disponivel', 'disponivel'), # Define valores permitidos para o campo status
        ('ALUGADO', 'alugado')
    ]

    nome = models.CharField(max_length=100)
    email = models.CharField(max_length=100)
    tipo = models.CharField(max_length=100)
    titulo = models.CharField(max_length=50)
    valor_aluguel = models.DecimalField(max_digits=10, decimal_places=2) # pesquisar
    status = models.CharField(max_length=20, choices=STATUS_CHOICES)
    locador = models.ForeignKey(Usuario, on_delete=models.CASCADE, related_name='imoveis')
                
    def __str__(self):
        return self.titulo
                                
class Contrato (models.Model):
     
    data_inicio = models.DateField(max_length=100)
    data_fim = models.DateField(max_length=100)
    valor = models.DecimalField(max_digits=10, decimal_places=2)
    imovel = models.ForeignKey(Imovel, on_delete=models.CASCADE)
    locador = models.ForeignKey(Usuario, on_delete=models.CASCADE, related_name='contratos_locador')
    locatario = models.ForeignKey(Usuario, on_delete=models.CASCADE, related_name='contratos_locatario')

class Pagamento (models.Model):
    data_pagamento = models.DateField(max_length=100)
    valor = models.DecimalField(max_digits=10, decimal_places=2)
    status = models.CharField(max_length=100)
    contrato = models.ForeignKey(Contrato, on_delete=models.CASCADE, related_name='pagamentos')

    def __str__(self):
        return f'Pagamento de {self.valor}'



    

# Create your models here.

