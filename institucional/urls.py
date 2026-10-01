# -*- coding: utf-8 -*-
from django.urls import path
from . import views

urlpatterns = [
    path("", views.home, name="home"),
    path("sobre/", views.sobre, name="sobre"),
    path("servicos/", views.servicos, name="servicos"),
    path("neuroacesso/", views.neuroacesso, name="neuroacesso"),
    path("noticias/", views.noticias, name="noticias"),
    path("noticias/<slug:slug>/", views.noticia_detalhe, name="noticia_detalhe"),
    path("doacoes/", views.doacoes, name="doacoes"),
    path("contato/", views.contato, name="contato"),
]
