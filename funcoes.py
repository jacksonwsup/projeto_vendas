import sqlite3 
from pathlib import Path

ROOT_DIR = Path(__file__).parent
DB_NAME = 'vendas.db'
DB_FILE = ROOT_DIR / DB_NAME

con = sqlite3.connect(DB_FILE)
cur = con.cursor()

sql = """
CREATE TABLE IF NOT EXISTS produto (            id INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT,
                                                name TEXT NOT NULL,
                                                ean TEXT NOT NULL,
                                                valor REAL UNIQUE NOT NULL)"""
cur.execute(sql) 
print(sql)                                               
con.commit()
sql = """
CREATE TABLE IF NOT EXISTS cliente (            id INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT,
                                                name TEXT NOT NULL,
                                                phone TEXT NOT NULL,
                                                endereco TEXT NOT NULL,
                                                email TEXT UNIQUE NOT NULL)"""
cur.execute(sql)
print(sql) 
con.commit()
sql = """                                             
CREATE TABLE IF NOT EXISTS venda (              id INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT,
                                                name TEXT NOT NULL,
                                                endereco TEXT NOT NULL,
                                                produtos TEXT NOT NULL,
                                                vtotal REAL NOT NULL)"""
cur.execute(sql)

def menu():
    
    selecao = input(
        
        '''
        SELECIONE A OPÇÃO DESEJADA
        
        1-------- CADASTRAR PRODUTOS
        1.1------ VISUALIZAR PRODUTOS CADASTRADOS
        2-------- CADASTRAR CLIENTE
        2.1------ VISUALIZAR CLIENTES CADASTRADOS
        3-------- EFETUAR VENDAS
        3.1------ VISUALIZAR VENDAS REALIZADAS
        
        '''
    )
    
    if selecao == "1":
        cadastroProduto()
    elif selecao =="1.1":
        mostraProduto()
    elif selecao == "2":
        cadastroCliente()
    elif selecao == "2.1":
        mostraCliente()
    elif selecao == "3":
        venda()
    else:
        mostrarVenda()
        

def cadastroProduto():
    nome  =  input("Digite o nome do produto     :       ")
    ean   =  input("Digite o GTIN/EAN            :       ")
    valor =  input("Digite o valor do            :       ")
    cur.execute("""
                INSERT INTO produto(name,ean,valor)
                VALUES (?,?,?)
                """, (nome,ean,valor))
    con.commit()
    print("Dados Salvos")
    con.close()
    if (con):
        con.close()
        print("SQL connection closed")

def mostraProduto():
    print(f'Ver Produtos Cadastrados')
    cur.execute("""SELECT * FROM produto""")
    rows = cur.fetchall()
    for row in rows:
       print(row)   
    
    
def cadastroCliente():
    nome        =  input("Digite seu nome                :       ")
    telefone    =  input("Digite seu telefone            :       ")
    endereco    =  input("Digite seu endereço            :       ")
    email       =  input("Digite seu e-mail              :       ")
    cur.execute("""
                INSERT INTO cliente(name,phone,endereco,email)
                VALUES (?,?,?,?)
                """, (nome,telefone,endereco,email))
    con.commit()
    print("Dados Salvos")
    con.close()
    if (con):
        con.close()
        print("SQL connection closed")
        
    return print(f'Cadastrar Cliente')

def mostraCliente():
    print(f'Ver Produtos Cadastrados')
    cur.execute("""SELECT * FROM produto""")
    rows = cur.fetchall()
    for row in rows:
       print(row)  
    
    return print(f'Visualizar Clientes Cadastrados')

def venda():
    return print(f'Realizar Vendas')

def mostrarVenda():
    return print(f'Visualizar Vendas')

def main():
    
    menu()

main()

con.close()