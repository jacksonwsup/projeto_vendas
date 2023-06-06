<<<<<<< HEAD
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

=======
import sqlite3

produtos = sqlite3.connect('vendas.db')

#Criar e demais operacoes no DB
cursor = produtos.cursor()

cursor.execute("""
CREATE TABLE produtos (
        id INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT,
        nome TEXT NOT NULL,
        ean INTEGER,
        valor FLOAT
);
""")


#Inserir dados teste no banco
cursor.execute("INSERT INTO produtos VALUES("Coca Cola 2L", 8896574821,10.25)")

>>>>>>> ed47a5102b3e667a9500772674ec37b9a881d024
produtos.commit()