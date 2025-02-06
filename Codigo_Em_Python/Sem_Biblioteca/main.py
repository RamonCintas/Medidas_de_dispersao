#==================================================
#Programa: Medidas de dispersão sem biblioteca
#Programador: Ramon Cintas Gomes
#==================================================

dados = open("Arquivo.txt","r") # Aqui é onde os dados são abertos no python
dados_brutos = dados.readlines() # Aqui os dados do Arquivo.txt é lido e armazenado em dados_brutos

l1=[] # lista vazia para armazenar os dados da lista de dados brutos e limpar os dados

resultado = 0.0 # variavel criada para servir de parametro para as definições para pegar o valor de retorno

for i in dados_brutos:  # esse for percorre a lista de dados_brutos e adiciona cada item a l1 e tira os caracteres especiais
    l1.append(i.rstrip())

lista1 = [float(i) for i in l1] # aqui transforma todos os dados da l1 em float e adiciona na lista1

def Tamanhodalista(resultado): # aqui no tamanho da lista é onde é feito todo o cálculo para saber qual o tamanho da lista para usar o valor nas demais contas
    Tamanhodalista = 0 # lista recebe valor zero
    for i in lista1: # percorre a lista 1
        Tamanhodalista = 1 + Tamanhodalista # a cada item que for encontrado na lista1 ele adiciona o valor 1 na variavel tamanhodalista e vai acumulando
    return(Tamanhodalista) # retorna o valor do tamanho da lista para ser usado nas demais contas

def ValorMaximo(resultado): # definição de valormaximo com os cálculos para encontrar o valor maximo de uma lista
    lista1.sort(reverse = True) # a lista 1 é ordenada do maior para o menor
    maximo = lista1[0] # maximo recebe o primeiro valor da lista ordenada do maior para o menor
    return maximo # retorna o valor maximo da lista para o parametro resultado
    
def ValorMinimo(resultado):  # definição de valorminimo com os cálculos para encontrar o valor minimo de uma lista
    lista1.sort(reverse = False) # a lista 1 é ordenada do menor para o maior
    minimo = (lista1[0]) # minimo recebe o primeiro valor da lista ordenada do menor para o maior
    return minimo # retorna o valor minimo da lista para o parametro resultado

def Media(resultado): # aqui é onde a media é calculada
    media = 0 # media recebe 0
    valor = 0 # valor recebe 0
    for i in lista1: # percorre a lista 1
        valor = i + valor # para cada i na lista 1 o valor é adicionado mais o valor anterior
    media = (valor / Tamanhodalista(resultado))  # a media é feita com o valor dos Is somados e divididos pelo tamanho da lista 
    return media # Retorna o valor da media para o parametro resultado

def Mediana(resultado): # aqui é onde a mediana é calculada
    metade = Tamanhodalista(resultado) // 2 # Metade recebe o tamanho da lista e divide por 2 
    mediana = (lista1[metade - 1] + lista1[metade]) / 2 # mediana recebe a lista 1 com a metade -1 + lista1 metade dividido por 2 
    return mediana # retorna a mediana para o parametro resultado

def Variancia(resultado): # Aqui é onde é calculada a variancia
    var = 0 # var recebe zero
    for i in lista1: # percorre a lista1
        var = (((i - Media(resultado)) ** 2) + var) #Var recebe i - media potência de 2 + var anterior 
    Rvar = var / Tamanhodalista(resultado) # Rvar recebe a variavel var dividida pelo tamanho da lista 
    return Rvar # Rvar retorna o valor para o parametro resultado da definição variancia

def DesvioPadrao(resultado): # Aqui é onde é calculado o desvio padrão
    DVP = Variancia(resultado) ** (0.5) # DVP recebe a variancia e calcula a raiz do valor 
    return DVP # DVP retorna o valor para o parametro resultado da definição de desvio padrão
    
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
    print("|""Programa: Medidas de dispersão sem biblioteca\n|Programador: Ramon Cintas Gomes")
    print("|""------------------------------\n")
    print("|""------------------------------")
    print("|""Dados encontrados: ")
    print(l1)
    print("|""------------------------------\n")
    print("|""------ Sem biblioteca --------")
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
