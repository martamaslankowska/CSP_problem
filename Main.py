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




N = 5
matrix = np.empty(shape=(N, N), dtype=object)
variables = []
constraints = [RowEqualityConstraint(), ColumnEqualityConstraint()]
domain = list(range(1, N + 1))

index = 0
for i in range(N):
    for j in range(N):
        variables.append(Variable(i, j, c.copy(domain)))
        matrix[i][j] = variables[index]
        index += 1

problem = Problem(matrix, variables, constraints)
print(problem.forward_checking())


# var = matrix[2][1]
# matrix[2][3].domain = []
# var.value = 3
# print('\nResult:', problem.adjust_domains(var))
#
# var.get_domain()
# matrix[2][3].get_domain()
# matrix[2][2].get_domain()






