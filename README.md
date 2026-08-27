# 💻 Coding — ADS (2º Semestre)

Repositório oficial da disciplina **Coding**, do curso de **Análise e Desenvolvimento de Sistemas (ADS)**, referente ao **2º semestre**.

Aqui estão organizados os **códigos-fonte de todas as aulas**, exemplos práticos, exercícios e projetos desenvolvidos ao longo do curso.

---

## 📚 Sobre a disciplina

A disciplina tem como objetivo desenvolver o entendimento dos fundamentos da programação orientada a objetos e, em seguida, aplicar esses conhecimentos na construção de aplicações web utilizando o frameworks Django.

O conteúdo está dividido em duas grandes etapas:

1. **Programação Orientada a Objetos (POO)**
   Fundamentos da linguagem Python voltados à POO: classes, objetos, atributos, métodos, herança, polimorfismo, encapsulamento e abstração.

2. **Desenvolvimento Web com Django**
   Aplicação prática dos conceitos de POO na construção de projetos web utilizando o **framework Django**, incluindo models, views, templates, ORM, autenticação e deploy básico.

---

## 🐍 Linguagem e tecnologias

- **Linguagem:** Python 3.x
- **Framework (2ª etapa):** [Django](https://www.djangoproject.com/)
- **Gerenciador de pacotes:** pip / venv
- **Controle de versão:** Git e GitHub

---

## 📁 Estrutura do repositório

O repositório está organizado por aulas, seguindo a ordem cronológica do curso:

```
├── poo/
│   ├── aula-2026-mes-dia/
│   ├── aula-2026-mes-dia/
│   └── ...
│
├── django/
│   ├── aula-01-assunto/
│   ├── aula-02-assunto/
│   ├── aula-03-assunto/
│   └── ...
│
└── README.md
```

> Cada pasta de aula contém o código-fonte trabalhado em sala, comentários explicativos e, quando aplicável, um pequeno `README.md` local com instruções específicas.

---

## ⚙️ Como executar os códigos

### Pré-requisitos

- [Python 3.10+](https://www.python.org/downloads/) instalado
- [Git](https://git-scm.com/) instalado

### Clonando o repositório

```bash
git clone git@github.com:franciscocoelho-dev/Coding.git
cd Coding
```

### Criando um ambiente virtual (recomendado)

```bash
python -m venv venv

# Ativando o ambiente virtual
# Windows
venv\Scripts\activate

# Linux/Mac
source venv/bin/activate
```

### Instalando dependências (para os projetos Django)

```bash
pip install -r requirements.txt
```


### Executando um projeto Django

```bash
cd django/projeto-final
python manage.py runserver
```

---

## 🎯 Objetivos de aprendizagem

Ao final da disciplina, o(a) aluno(a) será capaz de:

- Compreender e aplicar os quatro pilares da POO;
- Estruturar códigos Python de forma modular e reutilizável;
- Desenvolver aplicações web utilizando o framework Django;
- Trabalhar com banco de dados através do ORM do Django;
- Utilizar Git/GitHub como ferramenta de versionamento de código.

---


## 👨‍🏫 Professor

Material desenvolvido e mantido pelo professor responsável pela disciplina de **Coding** — curso de **Análise e Desenvolvimento de Sistemas**.

---

## 📄 Licença

Este material é de uso educacional, disponibilizado para fins de estudo e acompanhamento da disciplina.
