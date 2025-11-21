# Sistema de Cadastro de Clientes (Python / JSON)

Este é um projeto simples de sistema CRUD (Create, Read, Update, Delete) desenvolvido em Python puro para gerenciamento básico de clientes. O objetivo principal foi implementar a persistência de dados utilizando o formato JSON para simular um banco de dados simples.

### ⚙️ Tecnologias Utilizadas

* **Linguagem Principal:** Python 3.x
* **Persistência de Dados:** Arquivo JSON
* **Controle de Versão:** Git & GitHub
* **Ambiente:** VS Code

**Pré-requisitos:**
* Ter o Python 3 instalado na sua máquina.

**Passos:**

1.  **Clone o repositório:**
    ```bash
    git clone [Link do seu repositório no GitHub]
    cd nome-da-pasta-do-seu-projeto
    ```
2.  **Execute o script principal:**
    ```bash
    python clientes.py
    ```
3.  O sistema será iniciado no terminal, exibindo o menu principal.

4.  ### ✨ Funcionalidades

O sistema oferece as seguintes opções através de um menu de console:
1.  **Cadastrar Novo Cliente:** Coleta dados (nome, CPF, telefone, etc.) e salva no arquivo `clientes.json`.
2.  **Visualizar Todos os Clientes:** Exibe a lista completa de cadastros.
3.  **Buscar Cliente:** Permite buscar por CPF ou Nome.
4.  **Excluir Cliente:** Remove um cadastro da lista e atualiza o arquivo JSON.
5.  **Sair do Programa:** Salva todas as alterações e encerra a aplicação.
