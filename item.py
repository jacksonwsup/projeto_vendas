import sqlite3 
from pathlib import Path


ROOT_DIR = Path(__file__).parent
DB_NAME = 'vendas.db'
DB_FILE = ROOT_DIR / DB_NAME

con = sqlite3.connect(DB_FILE)
cur = con.cursor()


class item:
    