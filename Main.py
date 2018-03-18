import numpy as np
from Problem import *
from Heuristic import *
import copy as c
import time
import os
import re

number_of_value_heuristics = 2
number_of_variable_heuristics = 4


# default problem is latin square --> square / graph
# default algorithm is backtracking --> back / forward
def algorithm(problem_type, algorithm_type, n, val, var):
    N = n
    matrix = np.empty(shape=(N, N), dtype=object)
    variables = []
    constraints = []
    value_heuristics = [InOrderValueHeuristic(), LeastConstrainedValueHeuristic()]
    variable_heuristics = [InOrderVariableHeuristic(), MostConstrainedVariableHeuristic(), MostConstrainingVariableHeuristic(), MostConstrainingOfMostConstrainedVariableHeuristic()]

    if problem_type == 'graph':
        constraints += [AdjacentNeighboursConstraint(), DiagonalNeighboursConstraint(), NonAdjacentNeighboursConstraint()]
        domain = list(range(1, 3))
    else:
        constraints += [RowEqualityConstraint(), ColumnEqualityConstraint()]
        domain = list(range(1, N+1))

    index = 0
    for i in range(N):
        for j in range(N):
            variables.append(Variable(i, j, c.copy(domain)))
            matrix[i][j] = variables[index]
            index += 1

    value_heuristic = value_heuristics[val]
    variable_heuristic = variable_heuristics[var]
    value_heuristic.set_constraints(constraints)
    variable_heuristic.set_constraints(constraints)

    problem = Problem(matrix, variables, constraints, value_heuristic, variable_heuristic)
    if algorithm_type == 'forward':
        res = problem.forward_checking()
    else:
        res = problem.backtracking()

    draw_matrix(matrix)
    return res


# runs algorithm() for many times with the same N and writes times to the file
def run_algorithm(problem_type, algorithm_type, N, nr_of_tests, val, var=0):
    file_name = problem_type + '_' + algorithm_type + '_N' + ('0' if N < 10 else '') + str(N)\
                + '_val' + str(val) + '_var' + str(var) + '_' + str(nr_of_tests) + '.txt'
    result = [str(N)]

    for i in range(nr_of_tests):
        start = time.perf_counter()
        algorithm(problem_type, algorithm_type, N, val, var)
        stop = time.perf_counter()
        t = (stop - start)
        print(t)
        result += [str(t)]

    print(file_name, '- done :)')
    with open(file_name, 'w+') as file_output:
        file_output.write('\n'.join(result))


# reads from files of given name the times and parameters
def read_many_files(problem_type, algorithm_type, nr_of_tests, var):
    all_files = []
    for i in range(number_of_value_heuristics):
        file_names = problem_type + '_' + algorithm_type + '_N..' + '_val' + str(i) + '_var' + str(var) + '_' + str(nr_of_tests) + '.txt'
        files = [f for f in os.listdir('.') if re.match(file_names, f)]
        files.insert(0, i)  # current val value
        files.insert(1, var)  # current var value
        all_files.append(files)
    return all_files  # list of lists


problem_types = ['square', 'graph']
algorithm_types = ['back', 'forward']

# problem_type = 'square'  # or 'graph'
# algorithm_type = 'forward'  # or 'forward'
# N = 5

# algorithm(problem_type, algorithm_type, N, 0, 0)

for pt in problem_types:
    for at in algorithm_types:
        for N in range(3,11):
            for heuristic in range(number_of_value_heuristics):
                run_algorithm(pt, at, N, 40, heuristic)


# run_algorithm(problem_type, algorithm_type, N, 25)
# files = read_many_files(problem_type, algorithm_type, 25, 0)
# draw_chart(problem_type, algorithm_type, files)

