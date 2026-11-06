import sqlite3
import datetime

conexao = sqlite3.connect('tratamento.db')
cursor = conexao.cursor()
cursor.execute("""
    CREATE TABLE IF NOT EXISTS tratamento (
        id INTEGER PRIMARY KEY,
        medicamento TEXT,
        posologia INTEGER,
        tempo INTEGER,
        inicio TEXT
    )
""")
conexao.commit()
conexao.close()

def adicionar_medicamento(medicamento, posologia, tempo):
    conexao = sqlite3.connect('tratamento.db')
    cursor = conexao.cursor()
    cursor.execute("INSERT INTO tratamento (medicamento, posologia, tempo, inicio) VALUES (?, ?, ?, ?)", (medicamento, posologia, tempo, datetime.datetime.now().strftime("%Y-%m-%d %H:%M")))
    conexao.commit()
    retorno = cursor.lastrowid
    conexao.close()
    return retorno

def listar_medicamentos():
    conexao = sqlite3.connect('tratamento.db')
    cursor = conexao.cursor()
    cursor.execute("SELECT * FROM tratamento")
    medicamentos = cursor.fetchall()
    conexao.close()
    return medicamentos

def listar_medicamento_por_id(id):
    conexao = sqlite3.connect('tratamento.db')
    cursor = conexao.cursor()
    cursor.execute("SELECT * FROM tratamento WHERE id = ?", (id,))
    medicamento = cursor.fetchone()
    conexao.close()
    return medicamento

def atualizar_medicamento(id, medicamento, posologia, tempo):
    conexao = sqlite3.connect('tratamento.db')
    cursor = conexao.cursor()
    cursor.execute("UPDATE tratamento SET medicamento = ?, posologia = ?, tempo = ? WHERE id = ?", (medicamento, posologia, tempo, id))
    conexao.commit()
    conexao.close()

def deletar_medicamento(id):
    conexao = sqlite3.connect('tratamento.db')
    cursor = conexao.cursor()
    cursor.execute("DELETE FROM tratamento WHERE id = ?", (id,))
    conexao.commit()
    conexao.close()

def listar_posologia_medicamento(medicamento):
    conexao = sqlite3.connect('tratamento.db')
    cursor = conexao.cursor()
    cursor.execute("SELECT posologia FROM tratamento WHERE medicamento = ?", (medicamento,))
    posologia = cursor.fetchone()
    conexao.close()
    return posologia

def listar_tempo_medicamento(medicamento):
    conexao = sqlite3.connect('tratamento.db')
    cursor = conexao.cursor()
    cursor.execute("SELECT tempo FROM tratamento WHERE medicamento = ?", (medicamento,))
    tempo = cursor.fetchone()
    conexao.close()
    return tempo

def listar_inicio_medicamento(medicamento):
    conexao = sqlite3.connect('tratamento.db')
    cursor = conexao.cursor()
    cursor.execute("SELECT inicio FROM tratamento WHERE medicamento = ?", (medicamento,))
    inicio = cursor.fetchone()
    conexao.close()
    return inicio
