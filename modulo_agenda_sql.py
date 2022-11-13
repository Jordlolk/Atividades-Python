# Agenda de Contatos
from multiprocessing import connection
from select import select
import sqlite3

def getConnection():
    #conectando
    connection = sqlite3.connect('agenda.db')
    #definindo um cursor
    cursor = connection.cursor()
    #criando a tabela(se não existir)
    cursor.execute("""
    CREATE TABLE IF NOT EXISTS contatos(
             id INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT,
             nome TEXT NOT NULL,
             fone TEXT 
    );          
    """) 
    #retorna a conexão
    return connection

def adiciona(nome, fone):
    connection = getConnection()
    cursor = connection.cursor()
    cursor.execute(f"""
    INSERT INTO contatos (nome,fone)
    VALUES ( '{nome}','{fone}')
    """)
    connection.commit()
    print("Contato Adicionado!")

def mostraContato(nome):
    connection = getConnection()
    cursor = connection.cursor()                                        
    linhas = cursor.execute(f"""

    SELECT nome FROM contatos WHERE nome = '{nome}'; 
    """).fetchall()
    print('\n'.join(map(lambda x: str(x[0]) , linhas))) 
    connection.close()
    print('Contado Adicionado!')
                    
def mostraLista():
    connection = getConnection()
    cursor = connection.cursor()
    linhas = cursor.execute("SELECT * FROM contatos;").fetchall()
    print('\n'.join(map(lambda x: str(x[0]) + ' ' + str(x[1]) + ' ' + str(x[2]), linhas))) 
    connection.close()
    
def apagaContato(nome):
    connection = getConnection()
    cursor = connection.cursor()
    cursor.execute(f"DELETE FROM contatos WHERE nome = '{nome}';").fetchall()
    connection.commit()
    print('\n')
    connection.close()
    print('Contato Apagado!')

def apagaTodosContatos():
    connection = getConnection()
    cursor = connection.cursor()
    cursor.execute(" DELETE FROM contatos");
    connection.commit()
    connection.close()
    