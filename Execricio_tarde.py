import tkinter as tk
from tkinter import ttk
import statistics
import matplotlib.pyplot as plt
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg

# Dados iniciais
pib = [150, 300, 500, 800, 150, 300, 900,100]
estados = ['SP', 'RS', 'BA', 'PE', 'ES', 'MT', 'MS', 'CE']
fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(12, 6))  # Subplots: gráfico de barras e estatísticas
bar_plot = ax1.bar(estados, pib, color='skyblue')
ax1.set_xlabel('Estados')
ax1.set_ylabel('PIB')
ax1.set_title('PIB por Estado')
ax1.set_xticks(range(len(estados)))
ax1.set_xticklabels(estados, rotation=0)
ax1.tick_params(axis='x')
ax1.grid(True)

# Configurações do subplot para estatísticas
ax2.axis('off')  # Desliga os eixos do subplot
stats_text = ax2.text(0.1, 0.9, '', transform=ax2.transAxes)  # Texto para exibir as estatísticas

def calcular_estatisticas(lista):
    media = statistics.mean(lista)
    mediana = statistics.median(lista)
    try:
        moda = statistics.mode(lista)
    except statistics.StatisticsError:
        moda = "Sem moda única"
    varianca = statistics.variance(lista)
    desvio = statistics.stdev(lista)
    menor = min(lista)
    maior = max(lista)
    return media, mediana, moda, varianca, desvio, menor, maior

def update_statistics(event):
    if event.xdata is not None:
        indice_estado = int(round(event.xdata))
        estado = estados[indice_estado]
        valor_pib = pib[indice_estado]

        media, mediana, moda, varianca, desvio, menor, maior = calcular_estatisticas(pib)

        stats_text.set_text(f'Média: {media:.2f}\n'
                           f'Mediana: {mediana:.2f}\n'
                           f'Moda: {moda}\n'
                           f'Variância: {varianca:.2f}\n'
                           f'Desvio padrão: {desvio:.2f}\n'
                           f'Menor: {menor:.2f}\n'
                           f'Maior: {maior:.2f}')

        fig.canvas.draw()

# Adiciona evento de clique nas barras do gráfico
for bar in bar_plot:
    bar.figure.canvas.mpl_connect('button_press_event', update_statistics)

def main():
    janela = tk.Tk()
    janela.title('Estatísticas e Gráficos de Empresas')

    canvas = FigureCanvasTkAgg(fig, master=janela)
    canvas.get_tk_widget().pack(side=tk.TOP, fill=tk.BOTH, expand=1)

    janela.mainloop()

if __name__ == "__main__":
    main()
