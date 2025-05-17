# Passo 1) Importar e instanciar o solver
from ortools.linear_solver import pywraplp

solver = pywraplp.Solver("Menor Caminho com Menos Arestas", pywraplp.Solver.GLOP_LINEAR_PROGRAMMING)

# Passo 2) Entrada de dados
n = int(input())      
s = int(input())      
T = int(input())      
aij = [[float(input()) for j in range(n)] for i in range(n)] 

# Passo 3) Variáveis de decisão (0 <= xij <= 1)
xij = [[solver.NumVar(0, solver.infinity(), f"x{i}{j}" for j in range(n)] for i in range(n)]

# Passo 4) Restrições de conservação de fluxo (garante que o fluxo segue uma linha reta da origem até o destino)
for i in range(n):
    restricao = 1 if i == s else -1 if i == T else 0
    ct = solver.Constraint(restricao, restricao)
    for j in range(n):
        ct.SetCoefficient(xij[i][j], 1)   # Fluxo saindo de i
        ct.SetCoefficient(xij[j][i], -1)  # Fluxo entrando em i
  
# Passo 5) Função objetivo (minimiza custo + penalidade de 1 por cada aresta)
BIG_M = 1e6  # Prioriza custo sobre número de arestas
objective = solver.Objective()
for i in range(n):
    for j in range(n):
        if xij[i][j] is not None:
            objective.SetCoefficient(xij[i][j], aij[i][j] * BIG_M + 1)
objective.SetMinimization()

# Passo 6) Resolver o problema
result = solver.Solve()

# Passo 7) Saída formatada
if result == pywraplp.Solver.OPTIMAL:
    custo_real = 0.0

    for i in range(n):
        for j in range(n):
            if xij[i][j] is not None:
                val = xij[i][j].solution_value()
                if val > 1e-6:
                    custo_real += aij[i][j]

    print("Solucao:")
    print(f"Valor objetivo = {custo_real:.1f}")

    for i in range(n):
        for j in range(n):
            val = xij[i][j].solution_value() if xij[i][j] is not None else 0.0
            if val < 1e-6:
                val = 0.0
            print(f"X{i}{j} = {val:.1f}")
