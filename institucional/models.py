# -*- coding: utf-8 -*-
from django.db import models


class InformacoesONG(models.Model):
    nome = models.CharField(max_length=200, default="ONG de Fisioterapia — Ricardo Leon Xavier")
    slogan = models.CharField(max_length=255, default="Reabilitação Neurofuncional, Dignidade e Tecnologia Assistiva")
    endereco = models.CharField(max_length=255, default="Av. Governador Mário Covas, 83 — Jardim Pignatary, Carapicuíba - SP")
    cep = models.CharField(max_length=20, default="06310-240")
    telefone = models.CharField(max_length=30, default="(11) 98765-4321")
    email = models.EmailField(default="contato@ricardoleon.auracloud.com.br")
    chave_pix = models.CharField(max_length=100, default="financeiro@ongricardoleon.org.br")
    horario_funcionamento = models.CharField(max_length=150, default="Segunda a Sexta-feira: 08:00 às 18:00")
    sobre_texto = models.TextField(
        default="A ONG de Fisioterapia coordenada por Ricardo Leon Xavier dedica-se ao acolhimento e reabilitação de pessoas com sequelas neurológicas motoras graves decorrentes de AVE, paralisia cerebral e traumas raquimedulares na região de Carapicuíba e Grande São Paulo. Aliamos calor humano, dedicação clínica e a vanguarda da tecnologia assistiva para devolver autonomia e esperança aos nossos assistidos."
    )
    missao = models.TextField(default="Democratizar o acesso à fisioterapia neurofuncional especializada de alta qualidade para famílias em vulnerabilidade social.")
    visao = models.TextField(default="Ser centro de referência comunitária em reabilitação motora humanizada integrada a inovações de bioengenharia e IoT.")
    valores = models.TextField(default="Empatia, Ética, Respeito à Dignidade Humana, Inovação Acessível e Transparência Social.")

    class Meta:
        verbose_name = "Informações da ONG"
        verbose_name_plural = "Informações da ONG"

    def __str__(self):
        return self.nome


class Servico(models.Model):
    titulo = models.CharField("Título do Serviço", max_length=150)
    icone = models.CharField("Ícone (Emoji ou Classe)", max_length=50, default="🧠")
    descricao_curta = models.CharField("Descrição Breve", max_length=255)
    detalhes = models.TextField("Detalhamento Clínico")
    destaque = models.BooleanField("Exibir em Destaque na Home", default=True)
    ordem = models.PositiveIntegerField("Ordem de Exibição", default=0)

    class Meta:
        verbose_name = "Serviço de Fisioterapia"
        verbose_name_plural = "Serviços de Fisioterapia"
        ordering = ["ordem", "titulo"]

    def __str__(self):
        return self.titulo


class Noticia(models.Model):
    titulo = models.CharField("Título", max_length=200)
    slug = models.SlugField("Identificador URL", unique=True)
    resumo = models.TextField("Resumo / Chamada")
    conteudo = models.TextField("Conteúdo da Notícia")
    categoria = models.CharField("Categoria", max_length=100, default="Atendimentos")
    data_publicacao = models.DateTimeField("Data de Publicação", auto_now_add=True)
    destaque = models.BooleanField("Destaque na Página Inicial", default=False)

    class Meta:
        verbose_name = "Notícia / Comunicado"
        verbose_name_plural = "Notícias e Transparência"
        ordering = ["-data_publicacao"]

    def __str__(self):
        return self.titulo


class Depoimento(models.Model):
    nome = models.CharField("Nome do Paciente ou Familiar", max_length=150)
    condicao = models.CharField("Condição / Histórico", max_length=150, help_text="Ex: Reabilitação Pós-AVE há 10 meses")
    depoimento = models.TextField("Relato")
    estrelas = models.PositiveSmallIntegerField("Avaliação (1 a 5)", default=5)
    data = models.DateField("Data", auto_now_add=True)

    class Meta:
        verbose_name = "Depoimento"
        verbose_name_plural = "Depoimentos de Assistidos"
        ordering = ["-data"]

    def __str__(self):
        return f"{self.nome} ({self.condicao})"


class MensagemContato(models.Model):
    TIPO_CHOICES = [
        ("atendimento", "Solicitar Atendimento Fisioterapêutico"),
        ("voluntario", "Quero ser Voluntário"),
        ("doacao", "Quero Fazer uma Doação / Parceria"),
        ("duvida", "Dúvidas e Informações Gerais"),
    ]

    nome = models.CharField("Nome Completo", max_length=150)
    email = models.EmailField("E-mail")
    telefone = models.CharField("Telefone / WhatsApp", max_length=30)
    tipo = models.CharField("Finalidade do Contato", max_length=30, choices=TIPO_CHOICES, default="atendimento")
    mensagem = models.TextField("Mensagem")
    data_envio = models.DateTimeField("Data do Envio", auto_now_add=True)
    lida = models.BooleanField("Mensagem Visualizada", default=False)

    class Meta:
        verbose_name = "Mensagem Recebida"
        verbose_name_plural = "Mensagens e Voluntários"
        ordering = ["-data_envio"]

    def __str__(self):
        return f"{self.nome} - {self.get_tipo_display()} ({self.data_envio.strftime('%d/%m/%Y')})"
