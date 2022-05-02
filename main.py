from itertools import islice
import numpy as np
from itertools import combinations

""" extract main variables from the input file--> list= [cols, rows, number_iteration] """
def extract_parameters(x):
    l=[]
    with open(x, mode='r') as f:
        lines = f.read()
        first = lines.split('\n', 1)[0]
        a = first.split()
        cols = int(eval(a[0]))
        l.append(cols)
        rows = int(eval(a[1]))
        l.append(rows)
        number_iteration = int(eval(a[2]))
        l.append(number_iteration)
    return (l)

""" create an empty matrix with size= (rows, cols) """

def initiate_matrix(x):
    l=extract_parameters(x)
    dimensions = (l[1], l[0])
    GRID = np.zeros(dimensions, int)
    return (GRID)


""" update the initial matrix according to alive cells indicated in the input file"""

def tomatrix(GRID, x):
    with open(x, mode='r') as f:
        for line in islice(f, 1, None):
            x = int(line.split()[0])
            y = int(line.split()[1])
            GRID[y][x] = 1
    return (GRID)


""" display the matrix content to check matrix content after each operation """

def display_matrix(GRID, rows, cols):
    for i in range(rows):
        for j in range(cols):
            print (str(GRID[i][j]), end=' ')
        print ()


"""compute the number of alive neighbors for a specific cell"""

def cell_neighbors(GRID, j, i):

    changes = list(set(list(combinations([0, 1, -1, 1, 0, -1], 2))))
    changes.remove((0, 0))
    num = 0
    for c in changes:
        x = i + c[0]
        y = j + c[1]
        try:
            if GRID[x][y] == 1 and x >= 0 and y >= 0:
                num += 1
        except:
            pass

    return (num)


"""compute the next generation: one iteration """
""" the case of n iterations is implemented in the testprogram.py file"""

def compute_next_gen(GRID, rows, cols):
    ng = np.zeros((rows, cols), int)
    for i in range(cols):
        for j in range(rows):
            num = 0
            num=cell_neighbors(GRID, i, j)
            if num == 3:
                ng[j][i] = 1
            elif num < 2 or num > 3:
                ng[j][i] = 0
            else:
                ng[j][i] = GRID[j][i]

    return (ng)





