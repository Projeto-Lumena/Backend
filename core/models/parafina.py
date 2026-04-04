from django.db import models

class Parafina(models.Model):
    cor = models.CharField(max_length=50)
    quantidade = models.IntegerField()