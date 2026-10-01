# -*- coding: utf-8 -*-
from django.contrib import admin
from .models import InformacoesONG, Servico, Noticia, Depoimento, MensagemContato

# Personalizacao do Painel Administrativo para o Ricardo Leon
admin.site.site_header = "ONG de Fisioterapia — Ricardo Leon Xavier"
admin.site.site_title = "Gestão da ONG Ricardo Leon"
admin.site.index_title = "Painel Administrativo da ONG | Carapicuíba - SP"


@admin.register(InformacoesONG)
class InformacoesONGAdmin(admin.ModelAdmin):
    list_display = ("nome", "telefone", "email", "chave_pix")

    def has_add_permission(self, request):
        # Apenas permite uma única configuração institucional (singleton)
        return not InformacoesONG.objects.exists()


@admin.register(Servico)
class ServicoAdmin(admin.ModelAdmin):
    list_display = ("titulo", "icone", "descricao_curta", "destaque", "ordem")
    list_editable = ("destaque", "ordem")
    search_fields = ("titulo", "descricao_curta", "detalhes")


@admin.register(Noticia)
class NoticiaAdmin(admin.ModelAdmin):
    list_display = ("titulo", "categoria", "destaque", "data_publicacao")
    list_filter = ("categoria", "destaque", "data_publicacao")
    search_fields = ("titulo", "resumo", "conteudo")
    prepopulated_fields = {"slug": ("titulo",)}


@admin.register(Depoimento)
class DepoimentoAdmin(admin.ModelAdmin):
    list_display = ("nome", "condicao", "estrelas", "data")
    list_filter = ("estrelas", "data")
    search_fields = ("nome", "condicao", "depoimento")


@admin.register(MensagemContato)
class MensagemContatoAdmin(admin.ModelAdmin):
    list_display = ("nome", "tipo", "telefone", "email", "data_envio", "lida")
    list_filter = ("tipo", "lida", "data_envio")
    search_fields = ("nome", "email", "telefone", "mensagem")
    list_editable = ("lida",)
    readonly_fields = ("nome", "email", "telefone", "tipo", "mensagem", "data_envio")
