# -*- coding: utf-8 -*-
"""
Script de inicializacao de banco de dados e dados reais da ONG Ricardo Leon
"""
import os
import django

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "core.settings")
django.setup()

from django.contrib.auth.models import User
from institucional.models import InformacoesONG, Servico, Noticia, Depoimento

# 1. Criar superusuario para acesso administrativo do Ricardo Leon e equipe
if not User.objects.filter(username="admin").exists():
    User.objects.create_superuser("admin", "contato@ricardoleon.auracloud.com.br", "admin123")
    print("Superusuário 'admin' criado com sucesso! (Senha: admin123)")
else:
    print("Superusuário 'admin' já existe.")

# 2. Informações Institucionais da ONG
info, created = InformacoesONG.objects.get_or_create(
    id=1,
    defaults={
        "nome": "ONG de Fisioterapia — Ricardo Leon Xavier",
        "slogan": "Reabilitação Neurofuncional, Dignidade e Tecnologia Assistiva",
        "endereco": "Av. Governador Mário Covas, 83 — Jardim Pignatary, Carapicuíba - SP",
        "cep": "06310-240",
        "telefone": "(11) 98765-4321",
        "email": "contato@ricardoleon.auracloud.com.br",
        "chave_pix": "pix.ricardoleon@auracloud.com.br",
        "horario_funcionamento": "Segunda a Sexta-feira: 08:00 às 18:00",
        "sobre_texto": (
            "A ONG de Fisioterapia coordenada pelo fisioterapeuta Ricardo Leon Xavier atua há anos no acolhimento "
            "e recuperação de pacientes com lesões neurológicas motoras severas (AVE, traumatismos cranianos, "
            "lesões medulares e doenças degenerativas) em Carapicuíba e região. Com infraestrutura adaptada e "
            "atendimento humanizado, transformamos cada sessão em um passo firme rumo à independência e à dignidade."
        ),
        "missao": "Democratizar a fisioterapia neurofuncional de alta complexidade para famílias de baixa renda e assistidos com sequelas motoras.",
        "visao": "Consolidar-se como centro de referência filantrópica integrado a pesquisas de tecnologia assistiva e Internet das Coisas (IoT).",
        "valores": "Amor ao próximo, rigor técnico-clínico, empatia, inovação tecnológica inclusiva e transparência comunitária.",
    },
)
print("Informações da ONG configuradas.")

# 3. Serviços de Fisioterapia
servicos_data = [
    {
        "titulo": "Fisioterapia Neurofuncional Pós-AVE",
        "icone": "🧠",
        "descricao_curta": "Reabilitação neurológica voltada à recuperação da marcha, equilíbrio e controle motor pós-derrame.",
        "detalhes": (
            "Tratamento focado na neuroplasticidade cerebral através de exercícios motores repetitivos e orientados a tarefas funcionais. "
            "Auxilia na diminuição da hemiplegia, espasticidade e reinserção nas atividades diárias."
        ),
        "destaque": True,
        "ordem": 1,
    },
    {
        "titulo": "Reabilitação Motora e Marcha",
        "icone": "🏃",
        "descricao_curta": "Treino em barras paralelas e cinesioterapia ativa para recuperação da independência locomotora.",
        "detalhes": (
            "Protocolos individualizados para fortalecimento muscular, treino proprioceptivo, correção de marcha e fortalecimento "
            "do equilíbrio estático e dinâmico, prevenindo quedas."
        ),
        "destaque": True,
        "ordem": 2,
    },
    {
        "titulo": "Cinesioterapia e Mobilização Passiva",
        "icone": "🤲",
        "descricao_curta": "Preservação da amplitude articular e prevenção de encurtamentos para assistidos acamados ou cadeirantes.",
        "detalhes": (
            "Alongamentos graduados, mobilização suave de articulações e alívio de contraturas musculares em pacientes com mobilidade "
            "severamente reduzida."
        ),
        "destaque": True,
        "ordem": 3,
    },
    {
        "titulo": "Monitoramento NeuroAcesso (Tecnologia Assistiva)",
        "icone": "⚡",
        "descricao_curta": "Avaliação das respostas neurofuncionais durante as sessões através de biossensores de EEG e IoT.",
        "detalhes": (
            "Projeto desenvolvido com acadêmicos de Engenharia de Computação da UNIVESP, utilizando capacetes com módulos ADS1299 e ESP32 "
            "para acompanhar ondas cerebrais e respostas aos estímulos cinesioterápicos."
        ),
        "destaque": True,
        "ordem": 4,
    },
]

for s in servicos_data:
    Servico.objects.get_or_create(titulo=s["titulo"], defaults=s)
print("Serviços de fisioterapia cadastrados.")

# 4. Depoimentos
depoimentos_data = [
    {
        "nome": "Maria Helena Silveira",
        "condicao": "Filha de paciente assistido pós-AVE",
        "depoimento": "O acolhimento e a competência do Dr. Ricardo Leon trouxeram esperança para nossa família. Meu pai voltou a dar os primeiros passos.",
        "estrelas": 5,
    },
    {
        "nome": "Antônio Carlos Rocha",
        "condicao": "Paciente em reabilitação motora há 8 meses",
        "depoimento": "Aqui não somos apenas pacientes, somos tratados como família. A fisioterapia me devolveu a vontade de viver e a independência.",
        "estrelas": 5,
    },
    {
        "nome": "Fernanda Santos Lima",
        "condicao": "Assistida em reabilitação neurológica",
        "depoimento": "A dedicação de toda a equipe em Carapicuíba é inspiradora. Ter um espaço com tanto cuidado acessível faz toda a diferença.",
        "estrelas": 5,
    },
]

for d in depoimentos_data:
    Depoimento.objects.get_or_create(nome=d["nome"], defaults=d)
print("Depoimentos cadastrados.")

# 5. Notícias e Transparência
noticias_data = [
    {
        "titulo": "ONG do Ricardo Leon Lança Portal Oficial e Parceria com a UNIVESP",
        "slug": "ong-lanca-portal-oficial-parceria-univesp",
        "categoria": "Institucional",
        "resumo": "Nova presença digital na AuraCloud e projeto pioneiro de tecnologia assistiva NeuroAcesso marcam nova fase da instituição em Carapicuíba.",
        "conteudo": (
            "Com imensa alegria, a ONG de Fisioterapia Ricardo Leon Xavier dá as boas-vindas à comunidade através do seu novo portal web oficial. "
            "Desenvolvido no âmbito do Projeto Integrador VI da UNIVESP e hospedado na infraestrutura nacional AuraCloud (auracloud.com.br), o site "
            "oferece canal direto de agendamentos, prestação transparente de contas e captação de voluntários e doações.\n\n"
            "A parceria também viabiliza testes experimentais do projeto assistivo NeuroAcesso, trazendo biossensoriamento em tempo real para as sessões clínicas."
        ),
        "destaque": True,
    },
    {
        "titulo": "Campanha Permanente de Doações e Acolhimento Comunitário",
        "slug": "campanha-permanente-doacoes-acolhimento",
        "categoria": "Campanhas",
        "resumo": "Saiba como apoiar o custeio de atendimentos fisioterapêuticos para pessoas carentes com sequelas neurológicas graves.",
        "conteudo": (
            "Nossos atendimentos dependem do apoio da sociedade civil e de empresas parceiras. Através da nossa chave PIX oficial ou de doações de materiais "
            "terapêuticos, você ajuda a manter viva a reabilitação de mais de uma dezena de famílias em Carapicuíba.\n\n"
            "Visite nossa sede na Av. Governador Mário Covas, 83, ou faça sua doação online com segurança."
        ),
        "destaque": True,
    },
]

for n in noticias_data:
    Noticia.objects.get_or_create(slug=n["slug"], defaults=n)
print("Notícias cadastradas com sucesso.")

print("--> SEED CONCLUÍDO COM ÊXITO!")
