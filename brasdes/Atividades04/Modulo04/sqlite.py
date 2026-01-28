import sqlite3

con = sqlite3.connect("teste.bd")
cur = con.cursor()
cur.execute("""
CREATE TABLE IF NOT EXISTS contato (
    nome TEXT,
    endereco TEXT,
    telefone TEXT
)
""")
res = cur.execute("SELECT name FROM sqlite_master")
print(res.fetchall())

