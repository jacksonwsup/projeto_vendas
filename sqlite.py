import sqlite3
from sqlite3 import Error #captura dos erros caso exista


#metodo que contém o caminho do banco de dados:
def createDataBase(test):
        print(f'Criando Banco de Dados: {test}')
        
        
        #atributo para a conexão
        conn = vendas
        
        
        #criando exceção para testar a conexão com o banco de dados.
        try:
                #se não existir ele cria, e se existir ele abre a conexão
                conn = sqlite3.connect(test)       
                
                #criando tabelas
                
                        
                print(sqlite3.sqlite_version_info)         
        except Error as e:
                print("Erro:, {e}")
        finally:
                if conn:
                        conn.close()
        
if __name__ == '__main__':
        vendas = "C:/Users/jackson/Documents/vendas/projeto_vendas/vendas.db"
        createDataBase(vendas)

con = sqlite3.connect('vendas.db')

cr = con.cursor()

sql = """
CREATE TABLE cliente (          id INTERGER NOT NULL PRIMARY KEY AUTOINCREMENT,
                                name TEXT NOT NULL,
                                phone TEXT NOT NULL,
                                endereco TEXT NOT NULL,
                                email TEXT UNIQUE NOT NULL)
"""

#sql = """
#CREATE TABLE produto (          id INTERGER NOT NULL PRIMARY KEY AUTOINCREMENT,
#                                name TEXT NOT NULL,
#                                ean TEXT NOT NULL,
#                                valor FLOAT UNIQUE NOT NULL)
#"""
#
#
#sql = """
#CREATE TABLE venda (            id INTERGER NOT NULL PRIMARY KEY AUTOINCREMENT,
#                                name TEXT NOT NULL,
#                                endereco TEXT NOT NULL,
#                                produtos TEXT NOT NULL,
#                                valor_total FLOAT NOT NULL
#"""


cr.execute(sql)
con.commit()
con.close()



#produtos = sqlite3.connect('vendas.db')
#
##Criar e demais operacoes no DB
#cursor = produtos.cursor()
#
#cursor.execute("""
#CREATE TABLE produtos (
#        nome TEXT,
#        ean INTEGER,
#        valor FLOAT
#);
#""")
#
#
##Inserir dados teste no banco
#cursor.execute("INSERT INTO produtos VALUES('Coca Cola 2L',8896574821,10.25)")
#
#produtos.commit()