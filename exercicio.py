import statistics
import matplotlib.pyplot as plt

def moda1(lista):
    moda = statistics.mode(lista)
    print('Moda: ', moda)


def mediana1(lista):
    mediana = statistics.median(lista)
    print('Mediana: ', mediana)


def varianca1(lista):
    varianca = statistics.variance(lista)
    print('Variança: ', varianca)

def desvio1(lista):
    desvio = statistics.stdev(lista)
    print(f'Desvio padrão:  {desvio:.2f}')


def media1(lista):
    media = statistics.mean(lista)
    print('Media: ', media)



empresa1 = [1000,6000,1200,8000,1400]
empresa2 = [5000,4000,3000,2000,7000]
empresa3 = [1200,1300,8000,3000,15000]
empresa4 = [1400,1750,2000,4500,5900,7000]
cargos =['Analista', 'Gerente','Diretor', 'Estagiário', 'Dono']
def handle(lista, salarios):

    print('EMPRESA', salarios)
    print('----------------------------')
    media1(lista)
    mediana1(lista)
    moda1(lista)
    varianca1(lista)
    desvio1(lista)
    plt.title('Empresa 1')
    plt.plot(cargos, empresa1)
    plt.show()
    plt.title('Empresa 2')
    plt.plot(cargos, empresa2)
    plt.show()
    plt.title('Empresa 3')
    plt.plot(cargos, empresa3)
    plt.show()
    plt.title('Empresa 4')
    plt.plot(cargos, empresa4)
    plt.show()


handle(empresa1, empresa1)  
handle(empresa2, empresa2)   
handle(empresa3, empresa3) 
handle(empresa4, empresa4)

enter=input('enter para sair')
