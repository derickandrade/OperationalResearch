#import the linear solver from ORTOOLS
from __future__ import print_function
from ortools.linear_solver import pywraplp

solver = pywraplp.Solver('simple_lp_program', pywraplp.Solver.GLOP_LINEAR_PROGRAMMING)

#Parameters [x1,x2]
lb = [0,0] #lower bounds: 0 <= x1,x2
ub = [1,2] #upper bounds: x1 <= 1 ; x2 <= 2
f = [3,1] #function coeffiecients: (3 * x1); (1 * x2)
#a1 * x1 + a2 * x2 <=b1
a = [1,1] 
b = [2] 

#Creating the optimization problem numeric variables
#Format: solver.NumVar(lower bound, upper bound, label)
"""
x1 = solver.NumVar(0, 1, 'x1')
x2 = solver.NumVar(0, 2, 'x2')
"""
x1 = solver.NumVar(lb[0], ub[0], 'x1')
x2 = solver.NumVar(lb[1], ub[1], 'x2')

#First create the constraint according the limits

ct = solver.Constraint(-solver.infinity(), b[0] ,'ct')
#-infinity<= x1+x2 <= 2

#multiplicative coefficients
ct.SetCoefficient(x1,a[0])
ct.SetCoefficient(x2,a[1])

# Create the objective function, 3*x1 + x2
objective = solver.Objective()
# The function is mapped as f1*x1 + f2*x2

# Putting the multiplicative coef. of x1 and x2
objective.SetCoefficient(x1, f[0])
objective.SetCoefficient(x2, f[1])

# Set the problem as a maximization
objective.SetMaximization()

# Execute the solver
solver.Solve()

# Print the solution
print("Solution:")
print("Objective value =", objective.Value())
print("x1 =", x1.solution_value())
print("x2 =", x2.solution_value())
