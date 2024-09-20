from django.contrib import admin
from django.utils.translation import gettext_lazy as _
from datetime import datetime
from .models import CategoriaServico, TipoServico, Contratante, Contratado, Contrato
from django.contrib.auth.models import User, Group

# Personalizando o Django Admin
admin.site.site_header = "Organização Força"
admin.site.site_title = "Portal da Organização Força"
admin.site.index_title = "Bem-vindo ao painel administrativo da Organização Força"
admin.site.unregister(User)
admin.site.unregister(Group)

# Configuração do admin para Categoria de Serviço
@admin.register(CategoriaServico)
class CategoriaServicoAdmin(admin.ModelAdmin):
    search_fields = ['nome']
    actions = None

# Configuração do admin para Tipo de Serviço
@admin.register(TipoServico)
class TipoServicoAdmin(admin.ModelAdmin):
    list_filter = ['categoria']
    search_fields = ['nome', 'categoria__nome']
    list_display = ('nome', 'categoria__nome')
    actions = None

# Configuração do admin para Contratante
@admin.register(Contratante)
class ContratanteAdmin(admin.ModelAdmin):
    search_fields = ['nome', 'telefone', 'endereco']
    list_display = ('nome', 'telefone')
    actions = None

# Configuração do admin para Contratado
@admin.register(Contratado)
class ContratadoAdmin(admin.ModelAdmin):
    search_fields = ['nome', 'telefone', 'endereco']
    list_filter = ['tipos_servicos']
    actions = None
    list_display = ('nome', 'telefone', 'servicos_oferecidos')

    def servicos_oferecidos(self, obj):
        # Obtém os nomes dos serviços oferecidos pelo contratado
        return ", ".join([servico.nome for servico in obj.tipos_servicos.all()])
    
    servicos_oferecidos.short_description = 'Serviços Oferecidos'

# Configuração do admin para Contrato
@admin.register(Contrato)
class ContratoAdmin(admin.ModelAdmin):
    list_filter = ['situacao', 'data_realizacao', 'contratante', 'contratado']
    search_fields = [
        'contratante__nome',
        'contratado__nome',
        'servicos_contratados__nome',
        'observacoes'
    ]
    autocomplete_fields = ['contratante', 'contratado']
    actions = None
    list_display = ('contratante', 'contratado', 'data_formatada', 'situacao')

    # Método personalizado para exibir a data no formato dd/MM/yyyy
    def data_formatada(self, obj):
        return obj.data_realizacao.strftime('%d/%m/%Y')
    
    # Definir o nome da coluna no admin
    data_formatada.short_description = 'Data de Realização'
