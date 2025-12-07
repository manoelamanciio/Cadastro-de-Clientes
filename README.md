# 💾 Sistema de Cadastro de Clientes (Python / SQLite)

Este projeto evoluiu de um sistema simples baseado em JSON para um sistema CRUD (Create, Read, Update, Delete) com persistência de dados utilizando o **SQLite**. O foco é gerenciar o cadastro básico de clientes de forma mais robusta.

O objetivo principal foi implementar o CRUD com um banco de dados relacional leve e integrado, facilitando a gestão dos dados mesmo após o encerramento do programa.

---

## ⚙️ Tecnologias Utilizadas

| Tecnologia | Função |
| :--- | :--- |
| **Linguagem Principal** | Python 3.x |
| **Persistência de Dados** | **SQLite3** (Banco de dados leve e integrado) |
| **Interface** | CLI (Command Line Interface) |
| **Controle de Versão** | Git & GitHub |
| **Ambiente de Desenvolvimento** | VS Code |

---

## 🚀 Pré-requisitos e Instalação

### Pré-requisitos

* Ter o **Python 3** instalado na sua máquina.
* O módulo **`sqlite3`** é nativo do Python e não requer instalação adicional.

### Passos de Execução

1.  **Clone o repositório:**
    ```bash
    git clone [https://github.com/manoelamanciio/Cadastro-de-Clientes.git](https://github.com/manoelamanciio/Cadastro-de-Clientes.git)
    cd Cadastro-de-Clientes
    ```

2.  **Execute o script principal:**
    ```bash
    python clientes.py
    ```
    *O sistema será iniciado no terminal, exibindo o menu principal.*

---

## ✨ Funcionalidades

O sistema oferece as seguintes opções através de um menu de console:

* **Cadastrar Novo Cliente:** Coleta dados (nome, CPF, telefone, etc.) e salva permanentemente no arquivo do banco de dados (`clientes.db`).
* **Visualizar Todos os Clientes:** Exibe a lista completa de cadastros, lendo diretamente do SQLite.
* **Buscar Cliente:** Permite buscar um registro específico por **CPF** ou **Nome**.
* **Atualizar Cliente:** Permite modificar os dados de um cliente existente.
* **Excluir Cliente:** Remove um cadastro do banco de dados e salva a alteração permanentemente.
* **Sair do Programa:** Encerra a aplicação.

---
