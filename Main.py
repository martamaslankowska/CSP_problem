import numpy as np
from Problem import *
import copy as c
import time
import os
import re


# default problem is latin square --> square / graph
# default algorithm is backtracking --> back / forward
def algorithm(problem_type, algorithm_type, n):
    N = n
    matrix = np.empty(shape=(N, N), dtype=object)
    variables = []
    constraints = []

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

    problem = Problem(matrix, variables, constraints)
    if algorithm_type == 'forward':
        res = problem.forward_checking()
    else:
        res = problem.backtracking()
    return res


problem_type = 'square'  # or 'graph'
algorithm_type = 'back'  # or 'forward'
N = 3
nr_of_tests = 20

file_name = problem_type + '_' + algorithm_type + '_N' \
            + ('0' if N<10 else '') + str(N) + '_' + str(nr_of_tests) + '.txt'
result = [str(N)]

for i in range(nr_of_tests):
    start = time.perf_counter()
    algorithm(problem_type, algorithm_type, N)
    stop = time.perf_counter()
    t = (stop - start)
    print(t)
    result += [str(t)]

with open(file_name, 'w+') as file_output:
    file_output.write('\n'.join(result))


matching_files = problem_type + '_' + algorithm_type + '.*' + str(nr_of_tests) + '.txt'
files = [f for f in os.listdir('.') if re.match(matching_files, f)]
draw_chart(problem_type, algorithm_type, files)

# a = np.array([2,3,2,3,2,3])
# print(np.average(a))
# print(np.std(a))
