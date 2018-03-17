from Variable import Variable
from Constraint import *
from Draw import *

class Problem:

    def __init__(self, matrix, var, constr):
        self.matrix = matrix
        self.constraints = constr
        self.variables = var
        self.N = matrix.shape[0]


    def print_values(self):
        for i in range(self.N):
            for j in range(self.N):
                print('On ({0},{1}) we have value:'.format(i,j), self.matrix[i][j].value)

    def check_constraints(self, variable):
        print("\nVariable ({0},{1}) value:".format(variable.i, variable.j), variable.value)
        # variable.color = get_color(7)
        satisfies = True
        for c in self.constraints:
            c.current_variable(variable)
            sat = c.satisfies(self.matrix)
            if satisfies and not sat:
                satisfies = False
            print(c.__class__.__name__, '--> satisfies?', sat)
        # draw_matrix(self.matrix)
        return satisfies

    def backtracking(self):
        self.backtrack(self.variables)
        draw_matrix(self.matrix)

    def backtrack(self, var_free):
        if len(var_free) == 0:
            return True
        else:
            variable = var_free[0]
            for i in variable.domain:
                variable.value = i
                if self.check_constraints(variable):
                    result = self.backtrack(var_free[1:])
                    if result:
                        return result
            variable.value = 0
            return False;


