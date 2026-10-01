# -*- coding: utf-8 -*-
from django import forms
from .models import MensagemContato


class MensagemContatoForm(forms.ModelForm):
    class Meta:
        model = MensagemContato
        fields = ["nome", "email", "telefone", "tipo", "mensagem"]
        widgets = {
            "nome": forms.TextInput(
                attrs={
                    "class": "form-control",
                    "placeholder": "Seu nome completo",
                    "required": "required",
                }
            ),
            "email": forms.EmailInput(
                attrs={
                    "class": "form-control",
                    "placeholder": "exemplo@email.com",
                    "required": "required",
                }
            ),
            "telefone": forms.TextInput(
                attrs={
                    "class": "form-control",
                    "placeholder": "(11) 98765-4321",
                    "required": "required",
                }
            ),
            "tipo": forms.Select(
                attrs={
                    "class": "form-select",
                    "required": "required",
                }
            ),
            "mensagem": forms.Textarea(
                attrs={
                    "class": "form-control",
                    "rows": 4,
                    "placeholder": "Como podemos ajudar você ou como deseja contribuir com a ONG?",
                    "required": "required",
                }
            ),
        }
