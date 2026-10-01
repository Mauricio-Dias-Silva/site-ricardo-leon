# -*- coding: utf-8 -*-
from django.shortcuts import render, get_object_or_404, redirect
from django.contrib import messages
from .models import InformacoesONG, Servico, Noticia, Depoimento
from .forms import MensagemContatoForm


def get_ong_info():
    info = InformacoesONG.objects.first()
    if not info:
        info = InformacoesONG.objects.create()
    return info


def home(request):
    info = get_ong_info()
    servicos = Servico.objects.filter(destaque=True)[:6]
    noticias = Noticia.objects.all()[:3]
    depoimentos = Depoimento.objects.all()[:4]

    if request.method == "POST":
        form = MensagemContatoForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(
                request,
                "Sua mensagem foi enviada com sucesso para a equipe do Ricardo Leon! Entraremos em contato o mais breve possível.",
            )
            return redirect("home")
    else:
        form = MensagemContatoForm()

    context = {
        "info": info,
        "servicos": servicos,
        "noticias": noticias,
        "depoimentos": depoimentos,
        "form": form,
    }
    return render(request, "home.html", context)


def sobre(request):
    info = get_ong_info()
    return render(request, "sobre.html", {"info": info})


def servicos(request):
    info = get_ong_info()
    servicos_list = Servico.objects.all()
    return render(request, "servicos.html", {"info": info, "servicos": servicos_list})


def neuroacesso(request):
    info = get_ong_info()
    return render(request, "neuroacesso.html", {"info": info})


def noticias(request):
    info = get_ong_info()
    noticias_list = Noticia.objects.all()
    return render(request, "noticias.html", {"info": info, "noticias": noticias_list})


def noticia_detalhe(request, slug):
    info = get_ong_info()
    noticia = get_object_or_404(Noticia, slug=slug)
    outras_noticias = Noticia.objects.exclude(id=noticia.id)[:3]
    return render(
        request,
        "noticia_detalhe.html",
        {"info": info, "noticia": noticia, "outras_noticias": outras_noticias},
    )


def doacoes(request):
    info = get_ong_info()
    return render(request, "doacoes.html", {"info": info})


def contato(request):
    info = get_ong_info()
    if request.method == "POST":
        form = MensagemContatoForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(
                request,
                "Mensagem enviada com sucesso! A equipe da ONG Ricardo Leon agradece seu contato.",
            )
            return redirect("contato")
    else:
        form = MensagemContatoForm()

    return render(request, "contato.html", {"info": info, "form": form})
