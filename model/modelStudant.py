import sqlite3
class studanteModel():
    def __init__(self):
        self.conexao = sqlite3.connect('serpro')
        self.cursor = self.conexao.cursor()
        self.cursor.execute("CREATE TABLE IF NOT EXISTS"
                            '('
                    'id INTEGER PRIMARY KEY AUTOINCREMENT,'
                    'nome TEXT NOT NULL,'
                    'idade INTEGER NOT NULL,'
                    'peso REAL NOT NULL'
                             ')'
                             )
    def saveStudant (self,nome,idade,peso):
        self.cursor.execute("INSERT INTO tb_alunos (nome,idade,peso) VALUES (?,?,?)",(nome,idade,peso))
        self.conexao.commit()
        self.cursor.close()  
    