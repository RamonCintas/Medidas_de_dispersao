#==================================================
#Programa: Medidas de dispersão com biblioteca
#Programador: Ramon Cintas Gomes
#==================================================

import statistics as s # aqui é onde a biblioteca statistics é importada para o programa python e recebe o nome de s
import numpy as n # aqui é onde a biblioteca numpy é importada para o programa python e recebe o nome de n

dados = open("Arquivo.txt","r") # Aqui é onde os dados são abertos no python
dados_brutos = dados.readlines() # Aqui os dados do Arquivo.txt é lido e armazenado em dados_brutos

l1=[] # lista vazia para armazenar os dados da lista de dados brutos e limpar os dados

resultado = 0.0 # variavel criada para servir de parametro para as definições para pegar o valor de retorno

for i in dados_brutos: # esse for percorre a lista de dados_brutos e adiciona cada item a l1 e tira os caracteres especiais
    l1.append(i.rstrip())

lista = [float(i) for i in l1] # aqui transforma todos os dados da l1 em float e adiciona na lista1

def ValorMaximo(resultado): # definição de valormaximo com os cálculos para encontrar o valor maximo de uma lista 
    maximo = max(lista) # código max devolve o maior valor da lista
    return maximo # retorna o valor maximo da lista para o parametro resultado
    
def ValorMinimo(resultado): # definição de valorminimo com os cálculos para encontrar o valor minimo de uma lista 
    minimo = min(lista) # código min devolve o menor valor de uma lista
    return minimo # retorna o valor minimo da lista para o parametro resultado

def Media(resultado): # aqui é onde a media é calculada u
    media= round(s.mean(lista),2) # usa o código round e a função mean da biblioteca "s" para calcular a media de forma pronta
    return media # retorna o valor da media da lista para o parametro resultado

def Mediana(resultado): # aqui é onde a mediana é calculada
    mediana = round(s.median(lista),2) # usa o código round e a função median da biblioteca "s" para calcular a mediana de forma pronta
    return mediana # retorna o valor da mediana da lista para o parametro resultado

def Variancia(resultado): # Aqui é onde é calculada a variancia
    var = round(n.var(lista),2)# usa o código round e a função var da biblioteca "n" para calcular a variancia de forma pronta
    return var # retorna o valor da variancia da lista para o parametro resultado

def DesvioPadrao(resultado): # Aqui é onde é calculado o desvio padrão
    std = round(n.std(lista),2) # usa o código round e a função std Standard Deviation da biblioteca "n" para calcular o desvio padrão de forma pronta
    return std # retorna o valor do desvio padrão da lista para o parametro resultado

def mais(resultado):
    maisdedesviopadrao = round(Media(resultado) + DesvioPadrao(resultado), 3)
    return maisdedesviopadrao
    
def menos(resultado):
    menosdedesviopadrao = Media(resultado) - DesvioPadrao(resultado)
    return menosdedesviopadrao
    
def listaDedesvio(resultado):
    listaDedesvio = []
    listaDedesvio.append(["%.2f""---"%menos(resultado),"%.2f"%Media(resultado),"----""%.2f"%mais(resultado)])
    return listaDedesvio

def saída(): # Aqui é onde é criada a saída do programa
    print("|""------------------------------")
    print("|""Programa: Medidas de dispersão com biblioteca\n|Programador: Ramon Cintas Gomes")
    print("|""------------------------------\n")
    print("|""------------------------------")
    print("|""Dados encontrados: ")
    print(l1)
    print("|""------------------------------\n")
    print("|""------- Com biblioteca -------")
    print("|""------------------------------")
    print("|) Valor máximo: ")
    print("|>",ValorMaximo(resultado))
    print("|""------------------------------")
    print("|) Valor mínimo: ")
    print("|>",ValorMinimo(resultado))
    print("|""------------------------------")
    print("|) Média: ")
    print("|>","%.2f" % Media(resultado))
    print("|""------------------------------")
    print("|) Mediana: ")
    print("|>","%.2f" % Mediana(resultado))
    print("|""------------------------------")
    print("|) Variância: ")
    print("|>","%.2f" % Variancia(resultado))
    print("|""------------------------------")
    print("|) Desvio padrão: ")
    print("|>","%.2f" % DesvioPadrao(resultado))
    print("|""------------------------------\n")
    print("|""------------------------------")
    print("|) DesvioPadrão (-) Média (+) DesvioPadrão|\n")
    print("|>",listaDedesvio(resultado))
    print("|""------------------------------")
saída()
