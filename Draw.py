import numpy as np
import matplotlib.pyplot as plt

my_colors = ["#FFFFAA", "#FF5858", "#E57BAD", "#AC7BD8", "#83B0FC", "#83FCE4", "#97F276", "#FFFA55", "#FFB055"]


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


def draw_chart(problem_type, algorithm_type, files):

    for f in files:
        avg = np.average(f)


    x = np.array([1, 2, 3, 4, 5])
    y = np.power(x, 2)  # Effectively y = x**2
    e = np.array([0.5, 2.6, 3.7, 4.6, 5.5])

    plt.errorbar(x, y, e, linestyle='None', marker='^')

    plt.show()
