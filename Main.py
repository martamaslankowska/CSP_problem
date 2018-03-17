import numpy as np
from Problem import *
import copy as c


#  default problem is latin square
def backtracking(problem_type, n):
    N = n
    matrix = np.empty(shape=(N,N), dtype=object)
    variables = []
    constraints = []

    if problem_type == 'graph':
        constraints += [AdjacentNeighboursConstraint(), DiagonalNeighboursConstraint(), NonAdjacentNeighboursConstraint()]
        domain = list(range(1, 3))
    else:
        constraints += [RowEqualityConstraint(), ColumnEqualityConstraint()]
        domain = list(range(1, N+1))

    index = 0
    for i in range(N):
        for j in range(N):
            variables.append(Variable(i, j, c.copy(domain)))
            matrix[i][j] = variables[index]
            index += 1

    problem = Problem(matrix, variables, constraints)
    problem.backtracking()

# backtracking('graph', 8)



N = 4
matrix = np.empty(shape=(N, N), dtype=object)
variables = []
# constraints = [RowEqualityConstraint(), ColumnEqualityConstraint()]
constraints = [AdjacentNeighboursConstraint(), DiagonalNeighboursConstraint(), NonAdjacentNeighboursConstraint()]
domain = list(range(1, 8))

index = 0
for i in range(N):
    for j in range(N):
        variables.append(Variable(i, j, c.copy(domain)))
        matrix[i][j] = variables[index]
        index += 1

problem = Problem(matrix, variables, constraints)
print(problem.forward_checking())



# var = matrix[3][2]
# var.value = 3
#
# constr = NonAdjacentNeighboursConstraint()
# constr.current_variable(var)
# a = constr.adjust_domains(matrix)
# print(a)
# draw_matrix(matrix)







