from sympy import *

from sympy.solvers.solveset import linsolve


class TimeCalculate:
    def __init__(self):
        print("Software Inicializado!")

    def get_input(self,input):
        file1 = open('{}'.format(input), 'r')
        line = True
        list = []
        while line:
            # print("Line: {}".format(line.strip()))
            line = file1.readline()
            caractere = line.strip().split(" ")
            list.append(caractere)
        file1.close()
        # new_list=[[int(j) for j in i] for i in list]
        # print(new_list)
        return list

    def calculate(self,line1,line2):
        # line1 = [1, 40, 10, 5]
        # line2 = [20, 20, 20]

        # line1=[1,20,10,50]
        # line2=[10,14,15]

        # line1=[1,40,10,1]
        # line2=[20,21,21]



        t1, t2, t3 = symbols('t1 t2 t3')  # Define Symbols
        vMax = int(line1[2]) * t1
        DMax = (int(line1[2]) * t1 ** 2) / 2
        dMax = ((-int(line1[3]) * t2 ** 2) / 2) + int(line1[2]) * t1 * t2
        vFinal = int(line2[2])

        eq1 = Eq(DMax + dMax, int(line2[0]))
        eq2 = Eq(vMax - int(line1[3]) * t2, vFinal)

        sol = solve([eq1, eq2], [t1, t2])
        t=[0]*len(sol)
        n=0
        for qtd_variaveis in sol:
            for valor in qtd_variaveis:
                if valor>0 and valor>t[n]:
                    t[n]=valor
            n+=n

        #print(t)

        trecho_restante=int(line1[1])-int(line2[0])

        tempo3=0
        eq3=Eq((int(line1[2])*t3**2)/2+int(line2[2])*t3, trecho_restante)
        sol = solve(eq3, t3)
        for valor in sol:
            if valor>0:
                tempo3=valor

        tempo_total=tempo3+sum(t)
        return tempo_total

if __name__ == '__main__':
    calculate = TimeCalculate()
    lists = calculate.get_input("input.txt")
    #print(lists)
    for x in range(0,len(lists)):
        if len(lists[x])!=4:
            continue
        else:
            list_principal=lists[x]
            tempo = 0
            print("A quantidade que vai repetir é:",list_principal[0])
            for y in range(0,int(list_principal[0])):
                n=y+x+1
                print("Indice da linha secundária:",n)
                print(list_principal)
                print(lists[n])
                print("\n\n")
                tempo = calculate.calculate(list_principal, lists[n])
                #print(tempo)
                print("{:.2f}".format(round(N(tempo), 2)))

    # line1=[1,20,10,50]
    # line2=[10,14,15]
    # qtd_checkpoint=line1[0]
    # print(qtd_checkpoint)
    # tempo=0
    # for x in range(0,qtd_checkpoint):
    #     tempo=tempo+calculate.calculate(line1,line2)
    # print("{:.2f}".format(round(N(tempo), 2)))