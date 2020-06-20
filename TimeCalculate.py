#Importação da Biblioteca SymPy para Resolução de Sistemas Não Lineares
'''Necessária a instalação da biblioteca Sympy para execução do programa

pip install sympy
ou
conda install sympy

'''
from sympy import *
import sys

#Variáveis Auxiliares
k=0
show_value=False

#Classe Principal
class TimeCalculate:
    def __init__(self):
        #Checagem de Inicialização
        print("Programa desenvolvido por Matheus Terra")
        print("matheusfterra@hotmail.com")
        print("\n")
        print("Software Inicializado com Sucesso!")


    #Importação dos dados do TXT
    def get_input(self,input):
        #Abertura do Arquivo .TXT
        file1 = open('{}'.format(input), 'r')

        #Variavel Auxiliar
        line = True
        #Lista para armazenação
        list = []
        #Laço de Repetição para Carregar todas as Linhas do Documento
        while line:
            #Leitura  da Linha
            line = file1.readline()
            #Separação dos valores inteiros pelo Espaço
            caractere = line.strip().split(" ")
            #Acrescimo dos inteiros na Lista
            list.append(caractere)
        #Fechamento do Arquivo TXT
        file1.close()
        #Retorno da lista para o programa principal
        return list

    #Calculo dos valores
    def calculate(self,line1,line2,qtd_int):
        #Importação das varíaveis globais auxiliares
        global k,show_value
        #Contagem da iteração para casos de Rota em Multilinhas
        k+=1
        #Criação das variaveis para Cálculo matemático
        t1, t2, t3 = symbols('t1 t2 t3')  # Define Symbols
        #Variavel de Velocidade Máxima
        vMax = int(line1[2]) * t1
        #Distância onde alcança-se a Velocidade Máxima
        DMax = (int(line1[2]) * t1 ** 2) / 2

        #Distancia percorrida pela frenagem
        dMax = ((-int(line1[3]) * t2 ** 2) / 2) + int(line1[2]) * t1 * t2
        #Velocidade Conferida no Checkpoint
        vFinal = int(line2[2])
        #Formação das Equações através das Varíaveis
        eq1 = Eq(DMax + dMax, int(line2[0]))
        eq2 = Eq(vMax - int(line1[3]) * t2, vFinal)

        #Resolução das Equações
        sol = solve([eq1, eq2], [t1, t2])
        #Criação de lista para Resultados
        t=[0]*len(sol)
        #Variável Auxiliar
        n=0
        #Laço para atribuir apenas valores positivos à somatória do tempo
        for qtd_variaveis in sol:
            for valor in qtd_variaveis:
                if valor>0 and valor>t[n]:
                    t[n]=valor
            n+=n

        #Caso tenha passado pelo último Checkpoint, Calcula-se o Tempo, sem restrição de Velocidade,
        if qtd_int==k:
            show_value=True
            #Calcula-se o Tamanho restante
            trecho_restante=int(line1[1])-int(line2[0])

            tempo3=0
            #Formação da Última Equação
            eq3=Eq((int(line1[2])*t3**2)/2+int(line2[2])*t3, trecho_restante)
            #Resolução da Equação
            sol = solve(eq3, t3)
            #Atribuição de Valores Positivos
            for valor in sol:
                if valor>0:
                    tempo3=valor
            #Soma do Tempo Total
            tempo_total=tempo3+sum(t)
            k=0
        #Soma do Tempo Total
        else:
            tempo_total=sum(t)
        #Retorno do Tempo Total
        return tempo_total

#Programa Principal
if __name__ == '__main__':
    #Tenta executar o arquivo com o argumento sendo informado.
    '''
    EXECUTAR: python TimeCalculate.py input.txt
    OU: python TimeCalculate.py
    OBS: O arquivo input.txt deve estar localizado na mesma pasta.
    '''
    try:
        arg = sys.argv[2]
    except:
        arg='input.txt'

    #Criação do Objeto
    calculate = TimeCalculate()

    #Importação do arquivo TXT
    lists = calculate.get_input(arg)
    #Variável Auxiliar
    count = 1
    #Laço de Repetição para todas as linhas do TXT
    for x in range(0,len(lists)):

        #Caso seja uma linha de 3 itens, não faz nada
        if len(lists[x])!=4:
            continue
        #Caso seja uma linha de 4 itens, chama a função com a linha principal, e as demais linhas para Calculo dos tempos
        else:
            #Atribui a Linha principal
            list_principal=lists[x]
            tempo = 0

            #Executa a função de cálculo, a quantidade de vezes setada na linha principal.
            for y in range(0,int(list_principal[0])):

                n=y+x+1
                tempo = calculate.calculate(list_principal, lists[n],int(list_principal[0]))

                if show_value==True:
                    #Arrendonda o valor de tempo para duas casa decimais
                    print("O tempo usado para Percorrer a rota {} foi de: {:.2f}s".format(count,round(N(tempo), 2)))
                    #Acrescimo do Contador
                    count += 1
                    #Limpeza da variável auxiliar
                    show_value=False
                else:
                    pass

'''
Infelizmente, demandei muito tempo na interpretação e modelagem matemática e física do problema, 
e não consegui finalizar corretamente estre programa. O Software funciona bem para Rotas 
em que são passadas apenas 1 linha de parâmetros. Nos casos em que há mais de uma linha, não tive oportunidade de 
finalizar a lógica.

OBS. Para execução do projeto, é necessário a instalação da biblioteca Sympy, por meio do PIP ou Anaconda.

Agradeço a oportunidade.
Disponibilizo esta programação, assim como o arquivo Input.txt em meu repositório do GitHub

https://github.com/matheusfterra/ZGSolucoes

'''