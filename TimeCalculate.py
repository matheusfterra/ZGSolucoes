from sympy import *

from sympy.solvers.solveset import linsolve


class TimeCalculate:
    def __init__(self):
        print("Software Inicializado!")

    def calculate(self,line1,line2):
        # line1 = [1, 40, 10, 5]
        # line2 = [20, 20, 20]

        # line1=[1,20,10,50]
        # line2=[10,14,15]

        # line1=[1,40,10,1]
        # line2=[20,21,21]



        t1, t2, t3 = symbols('t1 t2 t3')  # Define Symbols
        vMax = line1[2] * t1
        DMax = (line1[2] * t1 ** 2) / 2
        dMax = ((-line1[3] * t2 ** 2) / 2) + line1[2] * t1 * t2
        vFinal = line2[2]

        eq1 = Eq(DMax + dMax, line2[0])
        eq2 = Eq(vMax - line1[3] * t2, vFinal)

        sol = solve([eq1, eq2], [t1, t2])
        t=[0]*len(sol)
        n=0
        for qtd_variaveis in sol:
            for valor in qtd_variaveis:
                if valor>0 and valor>t[n]:
                    t[n]=valor
            n+=n

        #print(t)

        trecho_restante=line1[1]-line2[0]

        tempo3=0
        eq3=Eq((line1[2]*t3**2)/2+line2[2]*t3, trecho_restante)
        sol = solve(eq3, t3)
        for valor in sol:
            if valor>0:
                tempo3=valor

        tempo_total=tempo3+sum(t)
        return tempo_total

if __name__ == '__main__':
    calculate = TimeCalculate()
    line1=[1,20,10,50]
    line2=[10,14,15]
    qtd_checkpoint=line1[0]
    print(qtd_checkpoint)
    tempo=0
    for x in range(0,qtd_checkpoint):
        tempo=tempo+calculate.calculate(line1,line2)
    print("{:.2f}".format(round(N(tempo), 2)))