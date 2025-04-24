from __future__ import print_function
from ortools.linear_solver import pywraplp

"""
Max:    3x1 + 5x2
            x1 <= 4 upper bound
            2x2 <= 12 upper bound
            3x1 + 2x2 <= 18
            x1, x2 >= 0 lower bounds
"""

solver = pywraplp.Solver('simple_lp_program', pywraplp.Solver.GLOP_LINEAR_PROGRAMMING)

# Definindo parâmetros
lb = [0, 0]
ub = [4, 6] 
f = [3, 5] # Coef. da função de maximização
a = [3, 2] # Coef. da função de restrição
b = [18] # Resultado da restrição

x1 = solver.NumVar(lb[0], ub[0], "x1")
x2 = solver.NumVar(lb[1], ub[1], "x2")

ct = solver.Constraint(-solver.infinity(), b[0], "ct") # -infinito <= b <= 18

ct.SetCoefficient(x1, a[0])
ct.SetCoefficient(x2, a[1])

objective = solver.Objective()

objective.SetCoefficient(x1, f[0])
objective.SetCoefficient(x2, f[1])

objective.SetMaximization()

solver.Solve()

print("Solucao:")
print("Valor objetivo =", objective.Value())
print("x1 =", x1.solution_value())
print("x2 =", x2.solution_value())