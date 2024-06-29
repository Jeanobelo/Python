import tkinter as tk
from tkinter import ttk
import statistics
import matplotlib.pyplot as plt
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg


empresas = {
    'Empresa 1': [1000, 6000, 1200, 8000, 1400],
    'Empresa 2': [5000, 4000, 3000, 2000, 7000],
    'Empresa 3': [1200, 1300, 8000, 3000, 15000],
    'Empresa 4': [1400, 1750, 2000, 4500, 5900]
}

cargos = ['Analista', 'Gerente', 'Diretor', 'Estagiário', 'Dono']

def calcular_estatisticas(lista):
    media = statistics.mean(lista)
    mediana = statistics.median(lista)
    moda = statistics.mode(lista)
    varianca = statistics.variance(lista)
    desvio = statistics.stdev(lista)
    menor = min(lista)
    maior = max(lista)
    return media, mediana, moda, varianca, desvio, menor, maior

def handle(nome_empresa):
    dados_empresa = empresas[nome_empresa]
    print(f'EMPRESA {nome_empresa}')
    print('----------------------------')
    media, mediana, moda, varianca, desvio , menor, maior = calcular_estatisticas(dados_empresa)

    plt.figure(figsize=(8, 6))
    plt.bar(cargos, dados_empresa, color='skyblue')
    plt.xlabel('Cargos')
    plt.ylabel('Salários')
    plt.title(f'Distribuição de Salários - {nome_empresa}')
    plt.text(0.05, 0.95, f'Menor: {menor:.2f}', transform=plt.gca().transAxes)
    plt.text(0.05, 0.90, f'maior: {maior:.2f}', transform=plt.gca().transAxes)
    plt.text(0.05, 0.85, f'Média: {media:.2f}', transform=plt.gca().transAxes)
    plt.text(0.05, 0.80, f'Mediana: {mediana:.2f}', transform=plt.gca().transAxes)
    plt.text(0.05, 0.75, f'Moda: {moda}', transform=plt.gca().transAxes)
    plt.text(0.05, 0.70, f'Variância: {varianca:.2f}', transform=plt.gca().transAxes)
    plt.text(0.05, 0.65, f'Desvio padrão: {desvio:.2f}', transform=plt.gca().transAxes)
    plt.xticks(rotation=45)
    plt.tight_layout()
    plt.show()

def main():
    janela = tk.Tk()
    janela.title('Estatísticas e Gráficos de Empresas')

    for nome_empresa in empresas:
        button = ttk.Button(janela, text=nome_empresa, command=lambda nome=nome_empresa: handle(nome))
        button.pack(pady=5)

    janela.mainloop()

if __name__ == "__main__":
    main()