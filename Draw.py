import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from Variable import Variable



my_colors = ["#FF5858", "#FF58C2", "#BD58FF", "#83B0FC", "#83FCE4", "#97F276", "#FFFA55", "#FFB055"]


from enum import Enum
class Color(Enum):
    RED = 0
    PINK = 1
    VIOLET = 2
    BLUE = 3
    AQUA = 4
    GREEN = 5
    YELLOW = 6
    ORANGE = 7


def get_color(enum_col):
    return my_colors[enum_col]


def draw_matrix(board, N):
    row, col = N, N
    matrix = np.zeros(shape=(row, col), dtype=int)
    for i in range(row):
        for j in range(col):
            var = board[i][j]
            a = var.get_value()
            matrix[i][j] = (Variable)(board[i][j]).value

    df = pd.DataFrame(matrix)

    size = int(row*0.8)
    plt.figure(1, figsize=(size, size))
    tb = plt.table(cellText=matrix, loc=(0,0), cellLoc='center')

    tc = tb.properties()['child_artists']
    for cell in tc:
        cell.set_height(1.0/row)
        cell.set_width(1.0/col)

    ax = plt.gca()
    ax.set_xticks([])
    ax.set_yticks([])

    tb._cells[(1, 0)].set_facecolor(get_color(1))

    plt.show()

    return tb


