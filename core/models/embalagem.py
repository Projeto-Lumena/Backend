from django.db import models

class Embalagem(models.Model):
    quantidade = models.IntegerField()
    
    class Meta:
        verbose_name = 'Embalagem'
        verbose_name_plural = 'Embalagens'