from __future__ import print_function
from ortools.linear_solver import pywraplp

"""
Max:    somatório de i até C: Li*xi
            xi <= Ei upper bound
            (somatório de i até C: Ti*xi)<=T
            xi >= 0 lower bounds
"""

N = int(input()) # Tamanho do conjunto C

solver = pywraplp.Solver('simple_lp_program', pywraplp.Solver.GLOP_LINEAR_PROGRAMMING)

# Definindo parâmetros
E = [] # = ub ; Limite superior pra cada elemento de C
L = [] # = f ; Coeficientes da função objetivo
Ti = [] # = a; Valor proporcional pra cada elemento de C

for i in range(0,N):
    E.append(float(input()))

for i in range(0, N):
    L.append(float(input()))

for i in range(0, N):
    Ti.append(float(input()))

T = float(input())

lb = 0

x = []

for i in range (0, N):
    x.append(solver.NumVar(lb, E[i], "x" + str(i+1)))

ct = solver.Constraint(-solver.infinity(), T, "ct") # -infinito <= ct <= T
objective = solver.Objective()

for i in range (0, N):
    ct.SetCoefficient(x[i], Ti[i])
    objective.SetCoefficient(x[i], L[i])

objective.SetMaximization()

solver.Solve()

print("Solucao:")
print("Valor objetivo = {:.1f}".format(objective.Value()))

for i in range (0, N):
    s = str(i + 1)
    print("x" + s + " = {:.1f}".format(x[i].solution_value()))
