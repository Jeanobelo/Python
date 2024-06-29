import tkinter as tk
from tkinter import ttk

def soma():
    n1 = float(input_entry2.get())
    n2 = float(input_entry2.get())
    soma = n1 + n2
    label_resultado


janela = tk.Tk()
janela.geometry('500x500')
janela.title('Testando Tkinter')


text_label = tk.Label(janela, text= 'Calculadora')
text_label.pack()

input_entry = tk.Entry(janela)
input_entry.pack()
input_entry2 = tk.Entry(janela)
input_entry2.pack()


botao_entry = tk.Entry(janela)
botao_entry.pack()

botao = tk.Button(janela, text= 'Clique aqui', command= soma)
botao.pack()

label_resultado = tk.Label(janela, text='Resultado')

janela.mainloop()