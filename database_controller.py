import sqlite3
from sqlite3 import Error

DB_FILE = "cadastro_clientes.db"

#DEF cria e retorna a conexão ocom o banco de dados
def criar_conexao():
    conn = None
    try:
        conn = sqlite3.connect(DB_FILE)
        return conn
    except Error as e:
        print(f"Erro ao conectar ao banco de dados: {e}")
        return None
    
def inicializar_banco():
    #Conecta e cria a tabela CLIENTES.
    conn = criar_conexao()
    if conn is not None:
        #Comando para criar a tabela com todos os campos.
        # CPF é definido UNIQUE para evitar duplicatas.
        sql_create_clientes_table = """CREATE TABLE IF NOT EXISTS CLIENTES (
        id INTEGER PRIMARY KEY,
        nome TEXT NOT NULL,
        idade INTEGER,
        telefone TEXT,
        email TEXT,
        cpf TEXT UNIQUE NOT NULL,
        endereco TEXT,
        cep TEXT,
        sexo TEXT,
        data_nascimento TEXT
        );
        """ # <-- a string SQL termina aqui!
            
        try:
            cursor = conn.cursor()
            cursor.execute(sql_create_clientes_table)
            return conn
        except Error as e:
            print(f"Erro ao criar a tabela: {e}")
        return None
    return None         

def inserir_cliente_db(conn, cliente):
    """insere um novo cliente no banco de dados e retorna o ID do novo cliente. """

    sql = '''INSERT INTO CLIENTES(nome, idade, telefone, email, cpf, endereco, cep, sexo, data_nascimento)
             VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?) '''

    # Mapeia o dicionario de cleinte para a ordem correta na tupla
    dados = (
        cliente['nome'], cliente['idade'], cliente['telefone'], cliente['email'], cliente['cpf'], cliente['endereco'], cliente['cep'],
         cliente['sexo'], cliente['data_nascimento']
    )

    try:
        cursor = conn.cursor()
        cursor.execute(sql, dados)
        conn.commit() # salva a transação no arquivo db
        return cursor.lastrowid
    except sqlite3.IntegrityError:
        print(f"Erro: CPF já cadastrado.")
        return -1
    except Error as e:
        print(f"Erro ao inserir cliente: {e}")
        return -1
    
def  selecionar_todos_clientes(conn):
    """ Deletea um cliente baseado no CPF."""
    sql = 'SELECT * FROM CLIENTES'

    try:
        cursor = conn.cursor()
        cursor.execute(sql)

        colunas = [description[0] for description in cursor.description]
        clientes = [dict(zip(colunas, row)) for row in cursor.fetchall()]

        return clientes
    except Error as e:
        print(f"Erro ao selecionar clientes: {e}")
        return []
    
def excluir_cliente_db(conn, cpf):
    """ Exclui um cliente baseado no CPF e retorna TRUE se foi excluido."""
    sql = 'DELETE FROM CLIENTES WHERE cpf=?'
    try:
        cursor = conn.cursor()
        cursor.execute(sql, (cpf,))
        conn.commit()
        return cursor.rowcount > 0
    except Error as e:
        print(f"Erro ao excluir clientes: {e}")
        return False    

        
