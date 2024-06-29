import tkinter as tk
from tkinter import ttk
import matplotlib.pyplot as plt
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg


def grafico():
    vendas_em_milhoes = [15, 20, 30, 6, 89, 15]
    meses = ['JAN', 'FEV', 'MAR', 'MAI', 'JUN', 'JUL']

    fig, ax = plt.subplots()
    #ax.bar(meses, vendas_em_milhoes)
    colors = ['gold', 'yellowgreen', 'lightcoral', 'lightskyblue', 'lightgreen', 'pink']
    ax.pie(vendas_em_milhoes, labels=meses, colors=colors, autopct='%1.1f%%', startangle=140)
    ax.set_xlabel("MESES")
    ax.set_ylabel("VENDAS (em milhões)")
    ax.set_title('GRÁFICO DE VENDAS')
    ax.grid(True)
   
    canvas = FigureCanvasTkAgg(fig, master=frame_grafico)
    canvas.draw()
    canvas.get_tk_widget().pack(side=tk.RIGHT, fill=tk.BOTH, expand=True)


root = tk.Tk()
root.title('Vendas')

frame_grafico = tk.Frame(root)
frame_grafico.pack()

btn = tk.Button(root, text="Mostrar Gráfico", command=grafico)
btn.pack(padx=10)

root.mainloop()
