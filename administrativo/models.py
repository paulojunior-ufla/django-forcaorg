from django.db import models

class CategoriaServico(models.Model):
    nome = models.CharField(max_length=100)

    def __str__(self):
        return self.nome

    class Meta:
        verbose_name = "Categoria"  # Nome no singular
        verbose_name_plural = "Categorias"  # Nome no plural
        ordering = ['nome']

class TipoServico(models.Model):
    nome = models.CharField(max_length=100)
    categoria = models.ForeignKey(CategoriaServico, on_delete=models.CASCADE, verbose_name="Categoria")

    def __str__(self):
        return self.nome
    
    class Meta:
        verbose_name = "Serviço"  # Nome no singular
        verbose_name_plural = "Serviços"  # Nome no plural
        ordering = ['nome']

class Contratante(models.Model):
    nome = models.CharField(max_length=200)
    telefone = models.CharField(max_length=20, verbose_name="Telefone de Contato")
    endereco = models.TextField(verbose_name="Endereço Completo")

    def __str__(self):
        return self.nome

    class Meta:
        verbose_name = "Contratante"  # Nome no singular
        verbose_name_plural = "Contratantes"  # Nome no plural
        ordering = ['nome']

class Contratado(models.Model):
    nome = models.CharField(max_length=200)
    telefone = models.CharField(max_length=20, verbose_name="Telefone de Contato")
    endereco = models.TextField(verbose_name="Endereço Completo")
    tipos_servicos = models.ManyToManyField(TipoServico, verbose_name="Serviços Oferecidos")

    def __str__(self):
        return self.nome

    class Meta:
        verbose_name = "Contratado"  # Nome no singular
        verbose_name_plural = "Contratados"  # Nome no plural
        ordering = ['nome']


class Contrato(models.Model):
    SITUACAO_CHOICES = [
        ('aberto', 'Aberto'),
        ('sucesso', 'Concluído com sucesso'),
        ('falha', 'Concluído sem sucesso'),
    ]

    data_realizacao = models.DateField(verbose_name="Data de Realização")
    servicos_contratados = models.ManyToManyField(TipoServico, verbose_name="Serviços Contratados")
    contratante = models.ForeignKey(Contratante, on_delete=models.CASCADE, verbose_name="Contratante")
    contratado = models.ForeignKey(Contratado, on_delete=models.CASCADE, verbose_name="Contratado")
    observacoes = models.TextField(blank=True, null=True, verbose_name="Observações")
    situacao = models.CharField(max_length=20, choices=SITUACAO_CHOICES, verbose_name="Situação do Contrato")

    def __str__(self):
        return "Contrato"

    class Meta:
        verbose_name = "Contrato"  # Nome no singular
        verbose_name_plural = "Contratos"  # Nome no plural
        ordering = ['-data_realizacao']
