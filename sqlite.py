import sqlite3

produtos = sqlite3.connect('vendas.db')

#Criar e demais operacoes no DB
cursor = produtos.cursor()

cursor.execute("""
CREATE TABLE produtos (
        nome TEXT,
        ean INTEGER,
        valor FLOAT
);
""")


#Inserir dados teste no banco
cursor.execute("INSERT INTO produtos VALUES('Coca Cola 2L',8896574821,10.25)")

produtos.commit()