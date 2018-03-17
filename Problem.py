from Variable import Variable
from Constraint import *
from Draw import *
import copy

class Problem:

    def __init__(self, matrix, var, constr):
        self.matrix = matrix
        self.constraints = constr
        self.variables = var
        self.N = matrix.shape[0]

    ''' BACKTRACKING 
        check_constraints(), backtracking() and recursive backtrack() 
    '''

    def check_constraints(self, variable):
        print("\nVariable ({0},{1}) value:".format(variable.i, variable.j), variable.value)
        satisfies = True
        for c in self.constraints:
            c.current_variable(variable)
            sat = c.satisfies(self.matrix)
            if satisfies and not sat:
                satisfies = False
            print(c.__class__.__name__, '--> satisfies?', sat)
        return satisfies

    def backtracking(self):
        result, graph = False, False
        domain_len = len(self.variables[0].domain)
        while not result:
            result = self.backtrack(copy.copy(self.variables))
            # changing domain size for L(2,1) coloring
            if not result:
                graph = True
                for v in self.variables:
                    domain = v.domain
                    domain += [max(domain) + 1]
                    domain_len = len(domain)

        #  drawing matrix with adjusted colors and title
        if graph:
            for v in self.variables:
                v.color = get_color(v.value)
            draw_matrix(self.matrix, len(domain))
        else:
            draw_matrix(self.matrix)
        return domain_len

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
            variable.value = -1
            return False;

    ''' FORWARD CHECKING
        adjust_domains(), fix_empty_domains(), check_if_any_empty_domains() 
        forward_checking() and recursive forward_check()
    '''

    def adjust_domains(self, variable):
        changed_variables = []
        for c in self.constraints:
            c.current_variable(variable)
            changed_variables += c.adjust_domains(self.matrix)

        print('\nChanged domains for variable ({0},{1}) with value = {2} and domian = {3}'.format(variable.i, variable.j, variable.value, variable.domain))
        for a, b in changed_variables:
            print('  ({0},{1}) --> {2}'.format(a.i, a.j, a.domain))

        # if there were empty domains, fix them and return False
        if self.check_if_any_empty_domains():
            print('  DOMAINS ARE EMPTY...............................')
            self.fix_empty_domains(changed_variables, variable)
            # draw_matrix(self.matrix)
            return False, []
        return True, changed_variables

    def fix_empty_domains(self, changed_variables, variable):
        print('  Fixing changed domains:')
        for var, val in changed_variables:
            var.domain += [val]
            var.domain.sort()
            print('    ({0},{1}) --> {2}'.format(var.i, var.j, var.domain))

    def check_if_any_empty_domains(self):
        for i in range(self.N):
            for j in range(self.N):
                if len(self.matrix[i][j].domain) == 0:
                    return True
        return False

    def forward_checking(self):
        result, graph = False, False
        domain_len = len(self.variables[0].domain)
        while not result:
            result = self.forward_check(copy.copy(self.variables))
            # changing domain size for L(2,1) coloring
            if not result:
                graph = True
                for v in self.variables:
                    domain = v.domain
                    domain += [max(domain) + 1]
                    domain_len = len(domain)

        #  drawing matrix with adjusted colors and title
        if graph:
            for v in self.variables:
                v.color = get_color(v.value)
            draw_matrix(self.matrix, len(domain))
        else:
            draw_matrix(self.matrix)
        return domain_len

    def forward_check(self, var_free):
        if len(var_free) == 0:
            return True
        else:
            variable = var_free[0]
            for i in variable.domain:
                variable.value = i
                found_empty_domains, changed_variables = self.adjust_domains(variable)
                if found_empty_domains:
                    result = self.forward_check(var_free[1:])
                    if result:
                        return result
                    self.fix_empty_domains(changed_variables, variable)
            variable.value = -1
            return False;
