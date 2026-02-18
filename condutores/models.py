from django.db import models

class Condutor(models.Model):
    foto = models.ImageField(
    upload_to='condutores/',
    null=True,
    blank=True)
    nome = models.CharField(max_length=100)
    cargo = models.CharField(max_length=100)
    equipamento = models.CharField(max_length=100)
    empresa = models.CharField(max_length=100)
    filial = models.CharField(max_length=100)

    criado_em = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.nome