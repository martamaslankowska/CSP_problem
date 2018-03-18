import copy

class BaseValueHeuristic:
    def __init__(self):
        self.nr = 0

    def set_constraints(self, constraints):
        self.constraints = constraints

    def sort_domain(self, variable, matrix):
        pass


class BaseVariableHeuristic:
    def __init__(self):
        self.nr = 0

    def set_constraints(self, constraints):
        self.constraints = constraints

    def sort_list(self, variable, matrix):
        pass


class InOrderValueHeuristic(BaseValueHeuristic):
    def __init__(self):
        super(InOrderValueHeuristic, self).__init__()

    def sort_domain(self, variable, matrix):
        variable.domain.sort()
        return variable.domain


class LeastConstrainedValueHeuristic(BaseValueHeuristic):
    def __init__(self):
        super(LeastConstrainedValueHeuristic, self).__init__()

    def sort_domain(self, variable, matrix):
        values, count = [], 0
        for val in variable.domain:
            variable.value = val
            count = 0
            for c in self.constraints:
                c.current_variable(variable)
                count += c.how_many_valuables_changing(copy.copy(matrix))
            values += [(val, count)]
        sorted_tuples = sorted(values, key=lambda el: el[1])
        variable.domain = [x[0] for x in sorted_tuples]
        return variable.domain


class InOrderVariableHeuristic(BaseVariableHeuristic):
    def __init__(self):
        super(InOrderVariableHeuristic, self).__init__()

    def sort_list(self, variables, matrix):
        variables = sorted(variables, key=lambda x: x.nr)
        return variables


class MostConstrainedVariableHeuristic(BaseVariableHeuristic):
    def __init__(self):
        super(MostConstrainedVariableHeuristic, self).__init__()

    def sort_list(self, variables, matrix):
        return variables


class MostConstrainingVariableHeuristic(BaseVariableHeuristic):
    def __init__(self):
        super(MostConstrainingVariableHeuristic, self).__init__()

    def sort_list(self, variables, matrix):
        return variables


class MostConstrainingOfMostConstrainedVariableHeuristic(BaseVariableHeuristic):
    def __init__(self):
        super(MostConstrainingOfMostConstrainedVariableHeuristic, self).__init__()

    def sort_list(self, variables, matrix):
        return variables