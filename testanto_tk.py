import tkinter as tk
from tkinter import ttk


def soma():
    try:
        n1 = float(input_entry.get())
        n2 = float(input_entry2.get())
        resultado = n1 + n2
        label_resultado.config(text=f'Resultado: {resultado}')
    
    except ValueError:
        label_resultado.config(text='Erro: Entradas inválidas')

janela = tk.Tk()
janela.geometry('500x200')
janela.title('Calculadora Tkinter')


tk.Label(janela, text='Digite o primeiro número:').pack()
input_entry = tk.Entry(janela)
input_entry.pack()

tk.Label(janela, text='Digite o segundo número:').pack()
input_entry2 = tk.Entry(janela)
input_entry2.pack()


botao = tk.Button(janela, text='Calcular Soma', command=soma)
botao.pack()


label_resultado = tk.Label(janela, text='Resultado: ')
label_resultado.pack()

janela.mainloop()
