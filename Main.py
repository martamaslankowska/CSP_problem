from Variable import Variable


import numpy as np
from Draw import *

N = 4
board = np.zeros(shape=(N,N), dtype=Variable)

var = Variable(5)
board[1][3] = var

draw_matrix(board, N)


