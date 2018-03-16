from Variable import Variable
from Constraint import *
import numpy as np
from Draw import *
from Problem import *

N = 3
board = np.empty(shape=(N,N), dtype=object)
variables = []
constraints = []
domain = list(range(1,(N+1)))

# filling matrix and list with empty variables
ind = 0
for i in range(N):
    for j in range(N):
        variables.append(Variable(i, j, domain))
        board[i][j] = variables[ind]
        ind += 1

# drawing matrix
# board[2][1].color = get_color(2)
# board[1][2].value = 20
# draw_matrix(board)

# filling list with constraints
constraints.append(RowEqualityConstraint())
constraints.append(ColumnEqualityConstraint())

square = Problem(board, variables, constraints)
# variables[1].value = 30
# board[2][1].value = 30
# square.check_constraints(variables[1])

square.fill_matrix_backtrack()


