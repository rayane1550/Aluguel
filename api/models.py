from django.db import models

class Usuario(model.Model): # class usuario
    nome = models.CharField(max_length=100)

    

# Create your models here.

