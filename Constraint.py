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
                matrix[i][col].color = get_color(0)  # light yellow color
        return True




