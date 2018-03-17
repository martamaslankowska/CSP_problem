import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from Variable import Variable

my_colors = ["#FFFFAA", "#FF5858", "#E57BAD", "#AC7BD8", "#83B0FC", "#83FCE4", "#97F276", "#FFFA55", "#FFB055"]


# from enum import Enum
# class Color(Enum):
#     RED = 1
#     PINK = 2
#     VIOLET = 3
#     BLUE = 4
#     AQUA = 5
#     GREEN = 6
#     YELLOW = 7
#     ORANGE = 8


def get_color(enum_col):
    return my_colors[enum_col]


def draw_matrix(board, colors=0):
    N = board.shape[0]
    row, col = N, N
    matrix = np.zeros(shape=(row, col), dtype=int)
    for i in range(row):
        for j in range(col):
            matrix[i][j] = board[i][j].value

    size = int(row*0.8)
    plt.figure(1, figsize=(size, size))
    tb = plt.table(cellText=matrix, loc=(0,0), cellLoc='center')

    for i in range(row):
        for j in range(col):
            tb._cells[(i, j)].set_facecolor(board[i][j].color)

    tc = tb.properties()['child_artists']
    for cell in tc:
        cell.set_height(1.0/row)
        cell.set_width(1.0/col)

    if colors > 0:
        plt.title("number of colors = {}".format(colors))

    ax = plt.gca()
    ax.set_xticks([])
    ax.set_yticks([])

    plt.show()


