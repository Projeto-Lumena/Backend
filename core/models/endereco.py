from django.db import models
from .user import User

class Endereco(models.Model):
    usuario = models.ForeignKey( User, on_delete=models.CASCADE)
    rua = models.CharField(max_length=100)
    numero = models.CharField(max_length=10)
    complemento = models.CharField(max_length=50, blank=True, null=True)
    bairro = models.CharField(max_length=50)
    cidade = models.CharField(max_length=50)
    estado = models.CharField(max_length=2)
    cep = models.CharField(max_length=10)
    tipo = models.CharField(max_length=100)
    
    class Meta:
        verbose_name = 'Endereço'
        verbose_name_plural = 'Endereços'