import sqlite3

coon = sqlite3.connect('produtos.db')

cursor = conn.cursor()

cursor.execute("""
CREATE TABLE produtos (
        id INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT,
        nome TEXT NOT NULL,
        ean INTEGER,
        valor FLOAT
);
""")

print ("Tabela criada com sucesso.")

coon.close()