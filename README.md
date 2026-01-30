# Sistema de Cadastro de Clientes (Python / SQLite)

Aplicação de linha de comando (CLI) desenvolvida em **Python** para gerenciar um cadastro de clientes com **persistência de dados em SQLite**. O sistema realiza operações básicas de CRUD (Create, Read, Update, Delete) diretamente no banco de dados e exibe um menu interativo no terminal.

Este projeto é ideal para demonstrar **conceitos de backend, lógica de programação em Python e uso de banco de dados leve (SQLite)** — competências relevantes para vagas de estágio em desenvolvimento de software.

---

## 🛠️ Tecnologias Utilizadas

- **Python 3**
- **SQLite3** (banco de dados relacional leve)
- **Git & GitHub** (controle de versão)

---

## 📋 Funcionalidades

Por meio de um menu interativo no terminal, o sistema permite:

- Cadastrar um novo cliente
- Listar todos os clientes cadastrados
- Buscar clientes por nome ou CPF
- Atualizar dados de um cliente existente
- Excluir clientes do banco de dados
- Sair do programa

Essas operações são salvas de forma permanente no banco SQLite (`cadastro_clientes.db`). :contentReference[oaicite:1]{index=1}

---

## ⏱️ Como executar localmente

### Pré-requisitos

- Ter **Python 3** instalado
- Git para clonar o repositório

### Passos

1. Clone o repositório:
   ```bash
   git clone https://github.com/manoelamanciio/Cadastro-de-Clientes.git

cd Cadastro-de-Clientes

python cadastro_clientes.py


