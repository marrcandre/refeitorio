from django.db import models

class Cardapio(models.Model):
    WEEKDAYS = [
        ('SEG', 'Segunda-feira'),
        ('TER', 'Terça-feira'),
        ('QUA', 'Quarta-feira'),
        ('QUI', 'Quinta-feira'),
        ('SEX', 'Sexta-feira'),
    ]

    dia = models.CharField(max_length=3, choices=WEEKDAYS, unique=True)
    proteina = models.CharField(max_length=100)
    opcao_vegetariana = models.CharField(max_length=100)
    acompanhamento = models.TextField()
    saladas = models.TextField()
    sobremesa = models.CharField(max_length=100)

    def __str__(self):
        return f"Cardápio de {dict(self.WEEKDAYS).get(self.day)}"

    class Meta:
        verbose_name = "Cardápio"
        verbose_name_plural = "Cardápios"