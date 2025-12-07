import tkinter as tk
from tkinter import messagebox
from tkinter import ttk
# Importa o modulo sqlite3, que lida com o banco de dados
from database_controller import inicializar_banco, inserir_cliente_db, selecionar_todos_clientes, excluir_cliente_db

# variavel para armazenar a conexão com o banco de dados sqlite3
conexao_db = None

def fechar_janela(janela_atual, root_menu):
    """Função genérica para fechar a janela atual e reexibir o menu."""
    janela_atual.destroy()
    root_menu.deiconify()# traz o menu principal de volta

def salvar_cliente_gui(campos_entrada, root_menu, janela_cadastro):
    """Lê os dados dos campos Entry e insere no banco de dados."""
    global conexao_db

    novoCliente = {
        "nome": campos_entrada['nome'].get(),
        "idade": campos_entrada['idade'].get(),
        "telefone": campos_entrada['telefone'].get(),
        "email": campos_entrada['email'].get(),
        "cpf": campos_entrada['cpf'].get(),
        "endereco": campos_entrada['endereco'].get(),
        "cep": campos_entrada['cep'].get(),
        "sexo": campos_entrada['sexo'].get(),
        "data_nascimento": campos_entrada['data_nascimento'].get(),
    }    

    if not novoCliente['nome'] or not novoCliente ['cpf']:
       messagebox.showerror("Erro de Cadastro", "Os campos Nome e CPF são obrigatorios.")
       return

    id_cliente = inserir_cliente_db(conexao_db, novoCliente)

    if id_cliente > 0:
        messagebox.showinfo("Sucesso!", f"Cliente '{novoCliente['nome']}'cadastrado com sucesso!")

        for campo in campos_entrada.values():
            campo.delete(0, tk.END)

    elif id_cliente== -1:
         messagebox.showwarning("Aviso", "Falha no cadastro. Verifique se o CPF já existe.")
    else: 
         messagebox.showerror("Erro Crítico", "Falha desconhecida ao tentar salvar no banco de dados.")    

def abrir_janela_cadastro(root_menu):
    """Cria a janela com o formulario de cadastro"""
    root_menu.withdraw()#esconde a janela principal

    cadastro_window = tk.Toplevel(root_menu)
    cadastro_window.title("Cadastro de Novo Cliente")
    cadastro_window.geometry("500x700")

    #frame para agrupar e organizar os campos com grid
    form_frame = tk.Frame(cadastro_window)
    form_frame.pack(padx=20, pady=20, fill='x')

    tk.Label(form_frame, text="Formulário de Cadastro", font=("Arial", 14,"bold")).grid(row=0, column=0, columnspan=2, pady=10)

    def criar_campo(texto, linha):
        tk.Label(form_frame, text=f"{texto}:").grid(row=linha, column=0, sticky='w', padx=5, pady=5)
    
        campo = tk.Entry(form_frame, width=40)
        campo.grid(row=linha, column=1, sticky='ew', padx=5, pady=5)
        return campo

    campos_entrada = {}
    campos_entrada['nome'] = criar_campo("Nome Completo", 1)
    campos_entrada['idade'] = criar_campo("Idade", 2)
    campos_entrada['telefone'] = criar_campo("Telefone com DDD", 3)
    campos_entrada['email'] = criar_campo("E-mail", 4)
    campos_entrada['cpf'] = criar_campo("CPF(Apenas números)", 5)
    campos_entrada['endereco'] = criar_campo("Endereco", 6)
    campos_entrada['cep'] = criar_campo("CEP", 7)
    campos_entrada['data_nascimento'] = criar_campo("Data de Nascimento", 8)
    campos_entrada['sexo'] = criar_campo("Sexo (H/M)", 9)

#Botão de ação: Salver o cliente DB
    btn_salvar = tk.Button(cadastro_window, text="SALVAR CLIENTE",
                       bg="#5CB85C", fg="white", height=2, 
                       command=lambda: salvar_cliente_gui(campos_entrada, root_menu, cadastro_window))
    btn_salvar.pack(pady=20, fill='x', padx=20)

#Botão para voltar ao menu
    btn_voltar = tk.Button(cadastro_window, text="< Voltar ao Menu",
                       command= lambda: fechar_janela(cadastro_window, root_menu))
    btn_voltar.pack(anchor='w', padx=20, pady=10)

#Faz com que, ao fechar a janela, ela volte ao menu
    cadastro_window.protocol("WM_DELETE_WINDOW", lambda: fechar_janela(cadastro_window, root_menu))

#Funções de vizualização

def abrir_janela_visualizacao (root_menu):
    #Cria a janela com a tabela (Treeview) de clientes.

    global conexao_db

    root_menu.withdraw()
    visualizacao_window = tk.Toplevel(root_menu)
    visualizacao_window.title("Lista de Clientes Cadastrados.")
    visualizacao_window.geometry("900x500")

    tk.Label(visualizacao_window, text="Clientes Cadastrados", font=("Arial", 16,"bold")).pack(pady=10)

    #Chama a função do backend p/ obter dados
    clientes = selecionar_todos_clientes(conexao_db)

    #Define as colunas do treeview
    colunas = ("ID", "Nome", "Telefone", "Email", "Endereço", "Idade", "Data de Nasc.")

    tabela = ttk.Treeview(visualizacao_window, columns=colunas, show='headings')

    #Configura o titulo e largura de cada coluna
    tabela.heading("ID", text="ID"); tabela.column("ID", width=40, anchor='center')
    tabela.heading("Nome", text="Nome"); tabela.column("Nome", width=150)
    tabela.heading("CPF", text="CPF"); tabela.column("CPF", width=100)
    tabela.heading("Telefone", text="Telefone"); tabela.column("Telefone", width=100)
    tabela.heading("Email", text="E-mail"); tabela.column("Email", width=150)
    tabela.heading("Endereço", text="Endereço"); tabela.column("Endereço", width=150)
    tabela.heading("Idade", text="Idade"); tabela.column("Idade", width=50 ,anchor='center')
    tabela.heading("Data Nasc.", text="Nascimento"); tabela.column("Data Nasc.", width=100)

# Inserir os dados do banco Treeview
    if clientes:
        for cliente in clientes:
            tabela.insert("", tk.END, values = (
                cliente['id'],
                cliente['nome'],
                cliente['cpf'],
                cliente['telefone'],
                cliente['email'],
                cliente['endereco'],
                cliente['idade'],
                cliente['data_nascimento'],
            ))                    

    tabela.pack(pady=10, padx=10, fill='both', expand=True)

    btn_voltar = tk.Button(visualizacao_window, text="< Voltar ao Menu",
                       command=lambda: fechar_janela(visualizacao_window, root_menu))
    btn_voltar.pack(pady=10)

    visualizacao_window.protocol("WM_DELETE_WINDOW", lambda: fechar_janela(visualizacao_window, root_menu))


def menuPrincipal_GUI():
    global conexao_db

    root = tk.Tk()
    root.title("Sistema de Gerenciamento de Clientes")
    root.geometry("600x400")
    
    menu_frame = tk.Frame(root)
    menu_frame.pack(pady=50)

    tk.Label(menu_frame, text="Menu Principal", font=("Arial", 16,"bold")).pack(pady=15)

    tk.Button(menu_frame, text="1. Cadastrar Novo Cliente",
              width=35, height=2,
              command=lambda: abrir_janela_cadastro(root)).pack(pady=5)
    
    tk.Button(menu_frame, text="2. Visualizar Todos os Clientes",
              width=35, height=2,
              command=lambda: abrir_janela_visualizacao(root)).pack(pady=5)
    
    tk.Button(menu_frame, text="5. Sair do Programa",
              width=35, height=2, bg="#D9534F",fg="white",
               command=root.quit).pack(pady=20)
    
    root.mainloop()
    

def adicionar_clientes():
    global conexao_db
    print("\n   Cadastro de Novo Cliente   ")

    #coleta de dados
    nome = input("Digite seu nome completo: ")
    idade = input("Idade: ")
    numeroTelefone = input ("Telefone com o DDD: ")
    emailCliente = input ("E-mail: ")
    cpf = input("CPF: ")
    enderecoCliente = input("Endereço: ")
    cepCliente = input("CEP: ")
    sexo = input("SEXO:  (H)  OU  (M)  ")
    dataNascimento = input("Data de nascimento: ")

    print("                      ")


    #Criação de Dicionario
    novoCliente = {
        "nome":nome,
        "idade":idade,
        "telefone":numeroTelefone,
        "email":emailCliente,
        "cpf":cpf,
        "endereco":enderecoCliente,
        "cep":cepCliente,
        "sexo":sexo,
        "data_nascimento":dataNascimento,

    }

    id_cliente = inserir_cliente_db(conexao_db, novoCliente) 

    if id_cliente > 0:
        print(f"Cleiinte {nome} cadastrado com sucesso!ID: {id_cliente}")
    elif id_cliente == -1:
        print(f"Falha no cadastro. Verifique se o CPF já existe.")

def visualizarClientes():
    global conexao_db
    print("\n   Lista de Cliente Cadastrados   ")

    clientes = selecionar_todos_clientes(conexao_db)

    if len(clientes) == 0:
        print("Nenhum cliente cadastrado ainda.")
    else:
        for cliente in clientes:
            print("                ")

            print(f"ID: {cliente['id']}")
            print(f"Nome: {cliente['nome']}")
            print(f"Idade: {cliente['idade']}")
            print(f"Telefone: {cliente['telefone']}")
            print(f"E-mail: {cliente['email']}")
            print(f"CPF: {cliente['cpf']}")
            print(f"Endereço: {cliente['endereco']}")
            print(f"CEP: {cliente['cep']}")
            print(f"Data de nascimento: {cliente['data_nascimento']}")
            print(f"SEXO: {cliente['sexo']}")
            print("                       ")


def buscar_clientes():
    global conexao_db
    print("\n    Buscar Clientes   ")
    
    #1.obter a informação de busca do usuário.
    termo_busca = input("Digite o CPF (somente números) ou o nome do cliente: ").strip()
    sql_busca = "SELECT * FROM CLIENTES WHERE cpf = ? OR nome LIKE ?"

    cursor = conexao_db.cursor()
    cursor.execute(sql_busca, (termo_busca, f'%{termo_busca}%'))
    cliente_econtrado = cursor.fetchone()

    if cliente_econtrado:
        colunas = [column[0] for column in cursor.description]
        cliente_dict = dict(zip(colunas, cliente_econtrado))

        print(f"\n Cliente Encontrado: {cliente_dict['nome']}")
        print("                       ")

        for chave, valor in cliente_dict.items():
            print(f"{chave.replace('_', ' ').title()}: {valor}")
        print("                         ")
    else:
        print (f"\n Cliente com CPF/Nome'{termo_busca}' não foi encontrado.")            


def excluir_cliente():
    global conexao_db
    print("\n     Excluir Cliente     ")

    cpf_excluir = input("Digite o CPF do cliente que deseja EXCLUIR: ").strip()
    cliente_removido = excluir_cliente_db(conexao_db, cpf_excluir)

    if cliente_removido:
        print(f"Cliente com CPF{cpf_excluir} foi EXCLUÍDO com sucesso!")
    else:
        print(f"Erro: Cliente com CPF {cpf_excluir} não foi encontrado.")    


#FUNÇÃO DE CONTROLE PRINCIPAL
def menuPrincipal():
    while True:
        print("\n     Menu do Restaurante     ")
        print("1. Cadastrar Novo Cliente")
        print("2. Visualizar Todos os Clientes")
        print("3. Buscar Cliente")
        print("4. Excluir Cliente")
        print("5. Sair do Programa")

        opcao = input("Escolha uma opção (1) (2) (3) (4) (5): ")

        if opcao == '1':
            adicionar_clientes()
        elif opcao == '2':
            visualizarClientes()
        elif opcao == '3':
            buscar_clientes()
        elif opcao == '4':  
            excluir_cliente()
        elif opcao == '5':
            if conexao_db:
                conexao_db.close()
            print("Obrigado por usar o sistema! Encerrando...")
            break
        else:
            print("Opção inválida. Tente novamente.")     


if __name__ == '__main__':
    conexao_db = inicializar_banco()

    if conexao_db:
        menuPrincipal_GUI()
    else:
        messagebox.showerror("Erro de Banco de Dados", "Não foi possível iniciar o banco de dados. Encerrando o sistema.")
       

