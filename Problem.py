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
        print("\nVariable value:", variable.value)
        variable.color = get_color(7)
        for c in self.constraints:
            c.current_variable(variable)
            satisfies = c.satisfies(self.matrix)
            print(c.__class__.__name__, '--> satisfies?', satisfies)
        draw_matrix(self.matrix)

    def fill_matrix_backtrack(self):
        domain = self.variables[0].domain
        for i in range(self.N):
            for j in range(self.N):
                var = self.matrix[i][j]
                d = domain[0]
                satisfies = False
                print('\nVariable ({0},{1})'.format(i,j))
                while d <= (max(domain)+1) and not satisfies:
                    var.value = d
                    print("  current value =", d)
                    for c in self.constraints:
                        c.current_variable(var)
                        satisfies = c.satisfies(self.matrix)
                        print("    ", c.__class__.__name__, '--> satisfies?', satisfies)
                        if not satisfies:
                            # d = domain[domain.index(d)+1]
                            d += 1
                            break
        draw_matrix(self.matrix)
