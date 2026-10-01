# 🌐 Portal Institucional — ONG de Fisioterapia Ricardo Leon Xavier

> **Projeto Integrador VI (PI VI) — Engenharia de Computação — UNIVESP (Polo Poá/SP)**  
> **Parceiro Comunitário:** Ricardo Leon Xavier  
> **Sede:** Av. Governador Mário Covas, 83 — Jardim Pignatary — Carapicuíba/SP  
> **Hospedagem & Deploy:** Nuvem AuraCloud (`auracloud.com.br`)

---

## 📋 Sobre o Projeto

Este portal web institucional foi desenvolvido em consonância com as metas pactuadas no **Plano de Ação** e no **Relatório Parcial** do Projeto Integrador VI da UNIVESP. O objetivo é dotar a ONG de Fisioterapia de Ricardo Leon Xavier de uma presença digital moderna, acolhedora e acessível ("Passaporte para o Mundo"), permitindo:

1. **Visibilidade Comunitária:** Apresentar a história, missão e tratamentos da instituição para famílias de Carapicuíba e Grande São Paulo;
2. **Captação de Recursos e Transparência:** Canal direto para doações via PIX, adesão de voluntários e parcerias corporativas;
3. **Autonomia de Gestão (CMS):** Painel administrativo intuitivo (*Django Admin*) para que Ricardo Leon e sua equipe cadastrem serviços, notícias e gerenciem mensagens de contato sem precisar de conhecimentos em programação;
4. **Integração com Tecnologia Assistiva (NeuroAcesso):** Divulgação da pesquisa de biossensoriamento e IoT (capacetes EEG vestíveis com ESP32 e ADS1299).

---

## 🛠️ Tecnologias Utilizadas

- **Back-end:** Python 3 + Framework Django 5 (Arquitetura MVT);
- **Banco de Dados:** SQLite (desenvolvimento local) e compatível com PostgreSQL (produção na AuraCloud);
- **Front-end:** HTML5 Semântico, CSS3 Responsivo (Vanilla CSS) e JavaScript com recursos de acessibilidade (Alto Contraste e ajuste de fonte WCAG 2.1);
- **Infraestrutura em Nuvem:** Plataforma AuraCloud (`auracloud.com.br`), com suporte a Docker e certificados SSL automáticos.

---

## 🚀 Como Executar o Projeto Localmente

### Opção 1: Pelo Atalho Rápido (Recomendado no Windows)
Dê um duplo clique no arquivo:
```
iniciar_site.bat
```
O navegador abrirá automaticamente em `http://127.0.0.1:8000`.

### Opção 2: Pelo Terminal / Prompt de Comando
```bash
# Entrar na pasta do projeto
cd site-ricardo-leon

# Iniciar o servidor de desenvolvimento
python manage.py runserver
```

Abra no seu navegador: [http://127.0.0.1:8000](http://127.0.0.1:8000)

---

## 🔐 Painel Administrativo (Gestão por Ricardo Leon)

Para acessar o painel de gerenciamento de conteúdos, notícias, serviços e mensagens:
- **URL:** [http://127.0.0.1:8000/admin/](http://127.0.0.1:8000/admin/)
- **Usuário:** `admin`
- **Senha:** `admin123`

---

## 📂 Estrutura de Arquivos

```
site-ricardo-leon/
├── core/                   # Configurações centrais do Django (settings, urls, wsgi)
├── institucional/          # Aplicação principal da ONG
│   ├── models.py           # Modelos de dados (ONG, Serviços, Notícias, Depoimentos, Contatos)
│   ├── views.py            # Regras de negócio e renderização de páginas
│   ├── admin.py            # Personalização do painel administrativo
│   ├── forms.py            # Formulários validados de contato e voluntariado
│   └── urls.py             # Rotas de navegação
├── templates/              # Páginas HTML acessíveis e responsivas
│   ├── base.html           # Cabeçalho, acessibilidade e rodapé
│   ├── home.html           # Página inicial completa
│   ├── sobre.html          # História de Ricardo Leon e da ONG
│   ├── servicos.html       # Tratamentos fisioterapêuticos
│   ├── neuroacesso.html    # Bioengenharia e projeto IoT UNIVESP
│   ├── noticias.html       # Transparência e comunicados
│   ├── doacoes.html        # Chave PIX e voluntariado
│   └── contato.html        # Formulário e mapa em Carapicuíba
├── static/                 # Folhas de estilo CSS e scripts JS
│   ├── css/style.css       # Design system nobre e responsivo
│   └── js/main.js          # Menu mobile, contraste e cópia do PIX
├── seed_data.py            # Script que povoou o banco com dados reais
├── iniciar_site.bat        # Inicializador em 1 clique
├── Dockerfile              # Imagem para deploy em nuvem
├── docker-compose.yml      # Orquestração na AuraCloud
└── requirements.txt        # Dependências do projeto
```
