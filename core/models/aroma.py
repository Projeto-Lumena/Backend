from django.db import models

class Aroma(models.Model):
    nome = models.CharField(max_length=50)
    quantidade = models.IntegerField()