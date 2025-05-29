# Passo 1) Importar e instanciar o solver.
from ortools.linear_solver import pywraplp

solver = pywraplp.Solver("Problema_de_Transporte", pywraplp.Solver.GLOP_LINEAR_PROGRAMMING)

# Passo 2) Receber os dados de entrada
M = int(input())  # Número de fazendas
N = int(input())  # Número de armazéns

# Matriz de custos M x N (custo de transporte de cada fazenda para cada armazém)
A = [[float(input()) for j in range(N)] for i in range(M)]

# Vetor de produção das fazendas (P_i)
P = [float(input()) for i in range(M)]

# Vetor de capacidade dos armazéns (S_j)
S = [float(input()) for j in range(N)]

# Passo 3) Variáveis de decisão
# xij = quantidade transportada da fazenda i para o armazém j
x = [[solver.NumVar(0, solver.infinity(), f'x_{i}_{j}') for j in range(N)] for i in range(M)]

# Passo 4) Restrições
# Restrição de produção: toda produção de cada fazenda deve ser escoada
for i in range(M):
    ct = solver.Constraint(P[i], P[i])  # = P_i
    for j in range(N):
        ct.SetCoefficient(x[i][j], 1)

# Restrição de capacidade: cada armazém não pode receber mais que sua capacidade
for j in range(N):
    ct = solver.Constraint(S[j], S[j])  # = S_j
    for i in range(M):
        ct.SetCoefficient(x[i][j], 1)

# Passo 5) Função objetivo - Minimizar o custo total de transporte
objective = solver.Objective()
for i in range(M):
    for j in range(N):
        objective.SetCoefficient(x[i][j], A[i][j])
objective.SetMinimization()

# Passo 6) Resolver o problema
status = solver.Solve()

# Passo 7) Exibir os resultados
if status == pywraplp.Solver.OPTIMAL:
    print(f'Valor objetivo = {objective.Value()}')
    
    # Imprimir a matriz de solução
    for i in range(M):
        fileira = []
        for j in range(N):
            fileira.append(f'{x[i][j].solution_value():.2f}')
        print('[ ' + ' '.join(fileira) + ' ]')
else:
    print('O problema não possui solução ótima.')
