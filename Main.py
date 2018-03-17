import numpy as np
from Draw import *
from Problem import *
import random

# LATIN SQUARE PROBLEM
# N = 3
# s_board = np.empty(shape=(N,N), dtype=object)
# s_variables = []
# s_constraints = []
# s_domain = list(range(1,(N+1)))
#
# # filling matrix and list with empty variables
# ind = 0
# for i in range(N):
#     for j in range(N):
#         s_variables.append(Variable(i, j, s_domain))
#         s_board[i][j] = s_variables[ind]
#         ind += 1
#
# # filling list with constraints
# s_constraints.append(RowEqualityConstraint())
# s_constraints.append(ColumnEqualityConstraint())
#
# square = Problem(s_board, s_variables, s_constraints)
# square.backtracking()



# GRAPH COLOURING L(2,1)

N = 3
g_board = np.empty(shape=(N,N), dtype=object)
g_variables = []
g_constraints = []
g_domain = list(range(1,3))

# filling matrix and list with empty variables
ind = 0
for i in range(N):
    for j in range(N):
        g_variables.append(Variable(i, j, g_domain, -1))  #, random.randint(1,2*N)))
        g_board[i][j] = g_variables[ind]
        ind += 1

# filling list with constraints
g_constraints.append(AdjacentNeighboursConstraint())
# g_constraints.append(NonAdjacentNeighboursConstraint())
g_constraints.append(DiagonalNeighboursConstraint())

graph = Problem(g_board, g_variables, g_constraints)
graph.backtracking()











