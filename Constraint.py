from Variable import Variable
from Draw import *


class BaseConstraint:
    id = 0  # static global variable

    def __init__(self):
        self.nr = BaseConstraint.id + 1
        BaseConstraint.id += 1

    def current_variable(self, variable):
        self.variable = variable

    def satisfies(self, matrix):
        pass

    def adjust_domains(self, matrix):
        pass


class RowEqualityConstraint(BaseConstraint):
    def __init__(self):
        super(RowEqualityConstraint, self).__init__()

    def satisfies(self, matrix):
        N = matrix.shape[0]
        row = self.variable.i
        col = self.variable.j

        for j in range(N):  # checking all variables in a row
            if j != col:
                if matrix[row][j].value == matrix[row][col].value:
                    matrix[row][j].color = get_color(1)  # red color
                    return False
                matrix[row][j].color = get_color(0)  # light yellow color
        return True


class ColumnEqualityConstraint(BaseConstraint):
    def __init__(self):
        super(ColumnEqualityConstraint, self).__init__()

    def satisfies(self, matrix):
        N = matrix.shape[0]
        row = self.variable.i
        col = self.variable.j

        for i in range(N):  # checking all variables in a row
            if i != row:
                if matrix[i][col].value == matrix[row][col].value:
                    matrix[i][col].color = get_color(1)  # red color
                    return False
                matrix[i][col].color = get_color(0)  # light good color
        return True


class AdjacentNeighboursConstraint(BaseConstraint):
    def __init__(self):
        super(AdjacentNeighboursConstraint, self).__init__()

    def satisfies(self, matrix):
        N = matrix.shape[0]
        row = self.variable.i
        col = self.variable.j
        satisfies = True
        # self.variable.color = get_color(7)

        if 0 < row:  # upper neighbour
            if abs(self.variable.value - matrix[row-1][col].value) < 2:
                satisfies = False
            #     matrix[row - 1][col].color = get_color(1)
            # else:
            #     matrix[row - 1][col].color = get_color(6)

        if row < (N-1):  # lower neighbour
            if abs(self.variable.value - matrix[row+1][col].value) < 2:
                satisfies = False
            #     matrix[row + 1][col].color = get_color(1)
            # else:
            #     matrix[row + 1][col].color = get_color(6)

        if 0 < col:  # left neighbour
            if abs(self.variable.value - matrix[row][col-1].value) < 2:
                satisfies = False
            #     matrix[row][col - 1].color = get_color(1)
            # else:
            #     matrix[row][col - 1].color = get_color(6)

        if col < (N-1):  # right neighbour
            if abs(self.variable.value - matrix[row][col+1].value) < 2:
                satisfies = False
            #     matrix[row][col + 1].color = get_color(1)
            # else:
            #     matrix[row][col + 1].color = get_color(6)

        return satisfies


class DiagonalNeighboursConstraint(BaseConstraint):
    def __init__(self):
        super(DiagonalNeighboursConstraint, self).__init__()

    def satisfies(self, matrix):
        N = matrix.shape[0]
        row = self.variable.i
        col = self.variable.j
        satisfies = True
        # self.variable.color = get_color(7)

        if 0 < row and 0 < col:  # upper left neighbour
            if abs(self.variable.value - matrix[row-1][col-1].value) < 1:
                satisfies = False
            #     matrix[row - 1][col - 1].color = get_color(1)
            # else:
            #     matrix[row - 1][col - 1].color = get_color(6)

        if row < (N-1) and 0 < col:  # lower left neighbour
            if abs(self.variable.value - matrix[row+1][col-1].value) < 1:
                satisfies = False
            #     matrix[row + 1][col - 1].color = get_color(1)
            # else:
            #     matrix[row + 1][col - 1].color = get_color(6)

        if 0 < row and col < (N-1):  # upper right neighbour
            if abs(self.variable.value - matrix[row-1][col+1].value) < 1:
                satisfies = False
            #     matrix[row - 1][col + 1].color = get_color(1)
            # else:
            #     matrix[row - 1][col + 1].color = get_color(6)

        if row < (N-1) and col < (N-1):  # lower right neighbour
            if abs(self.variable.value - matrix[row+1][col+1].value) < 1:
                satisfies = False
            #     matrix[row + 1][col + 1].color = get_color(1)
            # else:
            #     matrix[row + 1][col + 1].color = get_color(6)

        return satisfies



class NonAdjacentNeighboursConstraint(BaseConstraint):
    def __init__(self):
        super(NonAdjacentNeighboursConstraint, self).__init__()

    def satisfies(self, matrix):
        N = matrix.shape[0]
        row = self.variable.i
        col = self.variable.j
        satisfies = True
        # self.variable.color = get_color(7)

        if 1 < row:  # upper neighbour
            if abs(self.variable.value - matrix[row-2][col].value) < 1:
                satisfies = False
            #     matrix[row - 2][col].color = get_color(1)
            # else:
            #     matrix[row - 2][col].color = get_color(6)

        if row < (N-2):  # lower neighbour
            if abs(self.variable.value - matrix[row+2][col].value) < 1:
                satisfies = False
            #     matrix[row + 2][col].color = get_color(1)
            # else:
            #     matrix[row + 2][col].color = get_color(6)

        if 1 < col:  # left neighbour
            if abs(self.variable.value - matrix[row][col-2].value) < 1:
                satisfies = False
            #     matrix[row][col - 2].color = get_color(1)
            # else:
            #     matrix[row][col - 2].color = get_color(6)

        if col < (N-2):  # right neighbour
            if abs(self.variable.value - matrix[row][col+2].value) < 1:
                satisfies = False
            #     matrix[row][col + 2].color = get_color(1)
            # else:
            #     matrix[row][col + 2].color = get_color(6)

        return satisfies
