import tkinter as tk
from tkinter import messagebox
import sqlite3
import matplotlib.pyplot as plt
sqlite3.connect('meu_banco_de_dados.bd')
cursor = connect.cursor

#criar tabela
cursor.execute('''
CREATE TABLLE IF NOT EXISTS pessoas( id INTERGER PRIMERY KEY AUTOINCREMENT NOT NULL, nome TEXT NOT NULL, idade INTERGER NOT NULL, cidade TEXT NOT NULL)

''')

nome= "paula"
idade = 30
cidade = "sao paulo"

cursor.execute("""
INSERT INTO pessoas(nome, idade, cidade)
VALUES(?,?,?)
"""), (nome, idade, cidade)

conexao.commit()

cursor.execute("SELECT * FROM pessoas")
pessoas = cursor.fetchall()

for pessoa in pessoas:
    print(f""" ID: {pessoa[0]}, NOME: {pessoa[1]}, Cidade: {pessoa[2]} """)

    conexao.close()

def inserir_dados():
    nome = entrada_nome.get()
    idade = entrada_idade.get()
    cidade = entrada_cidade.get()

    if nome and idade.isdigit() and cidade:
        cursor.execute('''
        INSERT INTO pessoas(nome, idade, cidade)
        VALUES(?,?,?)
        ''',(nome, int(idade), cidade))

        conexao.commit()
        messagebox.showinfo('showinnfo', 'Dados Inseridos')
        entrada_nome.delete(0, tk.END)
        entrada_idade.delete(0, tk.END)
        entrada_cidade.delete(0, tk.END)
    else:
        messagebox.showwarning('Showwarning', 'Algo deu errado')
