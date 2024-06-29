import statistics
import matplotlib.pyplot as plt

# Função para calcular e exibir as estatísticas
def calcular_estatisticas(lista):
    media = statistics.mean(lista)
    mediana = statistics.median(lista)
    moda = statistics.mode(lista)
    varianca = statistics.variance(lista)
    desvio = statistics.stdev(lista)
    
    print(f'Média: {media:.2f}')
    print(f'Mediana: {mediana:.2f}')
    print(f'Moda: {moda}')
    print(f'Variância: {varianca:.2f}')
    print(f'Desvio padrão: {desvio:.2f}')
    
    return media, mediana, moda, varianca, desvio

# Dados das empresas
empresa1 = [1000, 6000, 1200, 8000, 1400]
empresa2 = [5000, 4000, 3000, 2000, 7000]
empresa3 = [1200, 1300, 8000, 3000, 15000]
empresa4 = [1400, 1750, 2000, 4500, 5900]
cargos = ['Analista', 'Gerente', 'Diretor', 'Estagiário', 'Dono']

# Função para lidar com cada empresa
def handle(empresa, nome_empresa):
    print(f'EMPRESA {nome_empresa}')
    print('----------------------------')
    media, mediana, moda, varianca, desvio = calcular_estatisticas(empresa)
    
    # Plotagem do gráfico
    plt.figure(figsize=(8, 6))
    plt.bar(cargos, empresa, color='skyblue')
    plt.xlabel('Cargos')
    plt.ylabel('Salários')
    plt.title(f'Distribuição de Salários - {nome_empresa}')
    plt.text(0.05, 0.85, f'Média: {media:.2f}', transform=plt.gca().transAxes)
    plt.text(0.05, 0.80, f'Mediana: {mediana:.2f}', transform=plt.gca().transAxes)
    plt.text(0.05, 0.75, f'Moda: {moda}', transform=plt.gca().transAxes)
    plt.text(0.05, 0.70, f'Variância: {varianca:.2f}', transform=plt.gca().transAxes)
    plt.text(0.05, 0.65, f'Desvio padrão: {desvio:.2f}', transform=plt.gca().transAxes)
    plt.xticks(rotation=45)
    plt.tight_layout()
    plt.show()

# Chamadas para cada empresa
handle(empresa1, 'Empresa 1')
handle(empresa2, 'Empresa 2')
handle(empresa3, 'Empresa 3')
handle(empresa4, 'Empresa 4')

input('Pressione Enter para sair')
