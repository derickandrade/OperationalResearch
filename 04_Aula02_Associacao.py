!pip install ortools

# Passo 1) Importar e instanciar o solver.
from ortools.linear_solver import pywraplp
import random

solver = pywraplp.Solver("Rótulo qualquer", pywraplp.Solver.GLOP_LINEAR_PROGRAMMING)

# As variáveis de decisão estão nas restrições.
# As restrições são lidas da direita pra esquerda.

# Passo 2) Parametrização.

# i e j crescem até n
#n = random.randint(1,3)
#aij = [[random.randint(1,10) for _ in range(n)] for _ in range(n)]
#n = 2
#aij = [[0.5,0.5],[0.5,0.5]]
#print(n,"\n", aij)

n = int(input())
aij = [[float(input()) for j in range(0,n)] for i in range(0, n)]

# Passo 3) Determinar variáveis de decisão

#xij = [[solver.NumVar(0,1, f"x{i}{j}") for j in range(n)] for i in range(n)]
#print(xij)

xij = [[solver.NumVar(0,1, f"x{i}{j}") for j in range(n)] for i in range(n)]


# Passo 4) Determinar restrições

for i in range(n):
    #ct = solver.Constraint(Lower Bound, Upper Bound)
    ct = solver.Constraint(1,1)
    for j in range(n):
        #ct.SetCoefficient(Variável de Decisão, Coeficiente Multiplicativo)
        ct.SetCoefficient(xij[i][j], 1)

for j in range(n):
    ct = solver.Constraint(1,1)
    for i in range(n):
        ct.SetCoefficient(xij[i][j], 1)

# Passo 5) Função objetivo

objective = solver.Objective()

for i in range(n):
    for j in range(n):
        objective.SetCoefficient(xij[i][j], aij[i][j])

objective.SetMaximization()

# Passo 6) Resolver o problema

result = solver.Solve()

if result == 0:
    print("Solucao: \nValor objetivo =", objective.Value())
    for i in range(n):
        for j in range(n):
            print(xij[i][j], "=", xij[i][j].solution_value())
