from django.db import models
from condutores.models import Condutor

class Avaliacao(models.Model):
    condutor = models.ForeignKey(Condutor, on_delete=models.CASCADE)
    criado_em = models.DateTimeField(auto_now_add=True)

    # DOCUMENTAÇÃO
    cnh_em_dia = models.BooleanField()
    clrv_em_dia = models.BooleanField()

    # TRANSMISSÃO
    experiencia_duas_caixas = models.BooleanField()
    transmissao_correta = models.BooleanField()

    # CHECAGEM DO EQUIPAMENTO
    checagem_geral = models.BooleanField()
    sistema_freios = models.BooleanField()
    regulagem_retrovisores = models.BooleanField()

    # MOVIMENTAÇÃO
    observa_ambiente = models.BooleanField()
    antecipa_paradas = models.BooleanField()
    freia_suavemente = models.BooleanField()
    distancia_adequada = models.BooleanField()
    respeita_sinalizacao = models.BooleanField()
    analisa_espaco = models.BooleanField()

    # TRÂNSITO
    distancia_seguranca = models.BooleanField()
    atencao_trafego = models.BooleanField()
    velocidade_adequada = models.BooleanField()
    volante_ambas_maos = models.BooleanField()
    centrado_faixa = models.BooleanField()
    usa_retrovisores = models.BooleanField()
    usa_buzina = models.BooleanField()
    sinaliza_faixa = models.BooleanField()
    sinaliza_pedestres = models.BooleanField()
    tempo_semaforo = models.BooleanField()
    sinaliza_saidas = models.BooleanField()

    # CONVERSÕES
    respeita_preferencial = models.BooleanField()
    sinaliza_conversao = models.BooleanField()
    faixa_antecipada = models.BooleanField()
    conversao_correta = models.BooleanField()
    velocidade_conversao = models.BooleanField()
    convergencia_suave = models.BooleanField()

    # ULTRAPASSAGENS
    retrovisores_ultrapassagem = models.BooleanField()
    sinaliza_ultrapassagem = models.BooleanField()
    buzina_ultrapassagem = models.BooleanField()
    visibilidade_via = models.BooleanField()
    retorno_seguro = models.BooleanField()

    # COMPORTAMENTO
    tolerancia = models.BooleanField()
    tranquilidade = models.BooleanField()
    cinto = models.BooleanField()
    paciencia = models.BooleanField()
    responsabilidade = models.BooleanField()

    observacoes = models.CharField(max_length=300, blank=True)

    resultado = models.CharField(
        max_length=10,
        choices=[('APROVADO', 'Aprovado'), ('REPROVADO', 'Reprovado')]
    )

class Avaliacao(models.Model):
    RESULTADO_CHOICES = [
        ('APROVADO', 'Aprovado'),
        ('REPROVADO', 'Reprovado'),
    ]

    condutor = models.ForeignKey(Condutor, on_delete=models.CASCADE)
    observacoes = models.CharField(max_length=300, blank=True)
    resultado = models.CharField(
        max_length=10,
        choices=RESULTADO_CHOICES,
        null=True,
        blank=True
    )
    criado_em = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.condutor.nome} - {self.resultado}"
