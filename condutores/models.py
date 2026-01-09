from django.db import models

class Condutor(models.Model):
    foto = models.ImageField(upload_to='condutores/', blank=True, null=True)
    nome = models.CharField(max_length=100)
    cargo = models.CharField(max_length=100)
    equipamento = models.CharField(max_length=100)
    empresa = models.CharField(max_length=100)
    filial = models.CharField(max_length=100)

    criado_em = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.nome