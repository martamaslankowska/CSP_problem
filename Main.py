from Variable import Variable
import numpy as np
from Draw import *

N = 4
board = np.empty(shape=(N,N), dtype=object)
for i in range(N):
    for j in range(N):
        board[i][j] = Variable()

draw_matrix(board)
board[2][1].color = get_color(2)
draw_matrix(board)
