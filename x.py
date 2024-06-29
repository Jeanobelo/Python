import statistics
import matplotlib.pyplot as plt

# Função para calcular e exibir as estatísticas
def calcular_estatisticas(lista):
    media = statistics.mean(lista)
    mediana = statistics.median(lista)
    moda = statistics.mode(lista)
    varianca = statistics.variance(lista)
    desvio = statistics.stdev(lista)
    
    return media, mediana, moda, varianca, desvio

# Dados das empresas
empresa1 = [1000, 6000, 1200, 8000, 1400]
empresa2 = [5000, 4000, 3000, 2000, 7000]
empresa3 = [1200, 1300, 8000, 3000, 15000]
empresa4 = [1400, 1750, 2000, 4500, 5900]
cargos = ['Analista', 'Gerente', 'Diretor', 'Estagiário', 'Dono']

empresas = [empresa1, empresa2, empresa3, empresa4]
nomes_empresas = ['Empresa 1', 'Empresa 2', 'Empresa 3', 'Empresa 4']

# Criar uma figura com subplots para cada empresa
fig, axs = plt.subplots(1, len(empresas), figsize=(15, 6), sharey=True)

for i, empresa in enumerate(empresas):
    media, mediana, moda, varianca, desvio = calcular_estatisticas(empresa)
    
    # Plotagem do gráfico de barras para cada empresa
    axs[i].bar(cargos, empresa, color='skyblue')
    axs[i].set_xlabel('Cargos')
    axs[i].set_title(nomes_empresas[i])
    axs[i].text(0.05, 0.85, f'Média: {media:.2f}', transform=axs[i].transAxes)
    axs[i].text(0.05, 0.80, f'Mediana: {mediana:.2f}', transform=axs[i].transAxes)
    axs[i].text(0.05, 0.75, f'Moda: {moda}', transform=axs[i].transAxes)
    axs[i].text(0.05, 0.70, f'Variância: {varianca:.2f}', transform=axs[i].transAxes)
    axs[i].text(0.05, 0.65, f'Desvio padrão: {desvio:.2f}', transform=axs[i].transAxes)

# Ajustar layout e mostrar o gráfico
plt.tight_layout()
plt.show()

input('Pressione Enter para sair')
