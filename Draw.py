import numpy as np
import matplotlib.pyplot as plt
import numpy.polynomial.polynomial as poly
# import multipolyfit as mpf


my_colors = ["#FFFFAA", "#FF5858", "#E57BAD", "#AC7BD8", "#83B0FC", "#83FCE4", "#97F276", "#FFFA55", "#FFB055"]
# list of colors for graphs - (line color, error color)
graph_colors = [('#0080FF', '#99CCFF'), ('#FF00FF', '#FF99FF'), ('#CC6600', 'FFB266'), ('#009900', '#AACD6D')]

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
    fig, ax = plt.subplots()

    for i in range(len(files)):
        file = files[i]
        x = []  # matrix size (N)
        y = []  # average time
        e = []  # standard deviation of time
        val = file[0]
        var = file[1]
        file = file[2:]
        file.sort()

        if len(file) > 0:
            for file_name in file:
                with open(file_name) as file123:
                    f = [line.rstrip('\n') for line in file123]
                # print(file_name)
                # print(f)
                x.append(int(f[0]))
                f = np.asarray(f[1:]).astype(np.double)
                # print('F:', f)
                y.append(np.average(f))
                e.append(np.std(f))

        x = np.asarray(x)
        y = np.asarray(y)
        e = np.asarray(e)

        if x.shape[0] > 0:
            ax.errorbar(x, y, e, ecolor=graph_colors[i][1], linestyle=':',
                         label="val = {0} | var = {1}".format(val, var), color=graph_colors[i][0], marker='.')
            ax.legend(loc="upper left", shadow=True, title="Heuristics", fancybox=True)
            plt.xlabel('size of matrix N')
            plt.ylabel('time [seconds]')
            plt.xticks(x)  # forces x axis to show only integers

            if problem_type == 'square' and algorithm_type == 'back':
                plt.title('Latin square with backtracking')
            if problem_type == 'square' and algorithm_type == 'forward':
                plt.title('Latin square with forward checking')
            if problem_type == 'graph' and algorithm_type == 'back':
                plt.title('L(2,1)-coloring with backtracking')
            if problem_type == 'graph' and algorithm_type == 'forward':
                plt.title('L(2,1)-coloring with forward checking')

    plt.show()
    plot_name = problem_type + '_' + algorithm_type + '_var' + str(var) + '.png'
    fig.savefig(plot_name)

    # coeffs = np.polyfit(x, y, deg=2)
    # x2 = np.arange(min(x), max(x), .01)  # use more points for a smoother plot
    # y2 = np.polyval(coeffs, x2)  # Evaluates the polynomial for each x2 value
    # plt.plot(x2, y2, label="deg=3", color='y')

