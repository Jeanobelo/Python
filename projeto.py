import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from tkinter import *
import sqlite3
import openpyxl




def carregar_dados_vendas():
    data = {
        'DATA': ['2024-01-01', '2024-01-02', '2024-01-03', '2024-01-04', '2024-01-05'],
        'VENDAS': [1000, 1200, 800, 1200, 900],
        'PRODUTO': ['Produto A','Produto B','Produto A','Produto B','Produto A'],
        'PRECO': [100, 120, 100, 120, 100],
        'QUANTIDADE':[10,10,8,10,9]
    }
    df_vendas = pd.DataFrame(data)
    df_vendas.to_excel('dados.xlsx', index = False)
    return df_vendas

def plotar_grafico_vendas():
    df_vendas = carregar_dados_vendas()

    fig, (ax1, ax2) = plt.subplots(2, 1, figsize=(10, 8))

    sns.barplot(data=df_vendas, x='DATA', y='VENDAS', ax=ax1, color = "green")
    ax1.set_title('Vendas ao Longo do Tempo')
    ax1.set_xlabel('Data')
    ax1.set_ylabel('Vendas')
    ax1.tick_params(axis='x', rotation=45)

    
    sns.barplot(data=df_vendas, x='DATA', y='QUANTIDADE', ax=ax2, color = "red")
    ax2.set_title('Quantidade Vendida ao Longo do Tempo')
    ax2.set_xlabel('Data')
    ax2.set_ylabel('Quantidade')
    ax2.tick_params(axis='x', rotation=45)

  
    plt.tight_layout()
    plt.show()


def criar_interface_grafica():
    root = Tk()
    root.title('Análise de Vendas')

    btn_plotar = Button(root, text='Plotar Gráficos de Vendas', command=plotar_grafico_vendas)
    btn_plotar.pack(pady=20)

    root.mainloop()

criar_interface_grafica()