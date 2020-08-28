#%% Insert path
import sys
sys.path.insert(0, "C:/Users/gemin/Documents/Repositories_personal/Python_packages/sudoku/sudoku")


#%% Import Libraries
import numpy as np
import timeit
from sudoku_solver import sudoku_solver
from sudoku_solver_dado3212 import *
from sudoku_examples import *


#%% Timeit

%timeit sudoku_solver(sudoku_easy2)

%timeit sudoku_solver(sudoku_easy3)

%timeit sudoku_solver(sudoku_medium3)

%timeit sudoku_solver(sudoku_hard3)

%timeit sudoku_solver(sudoku_expert3)

%timeit sudoku_solver(sudoku_16x16_beginner_1)

%timeit sudoku_solver(sudoku_16x16_confirmed_1)


## 1.21 ms ± 114 µs per loop (mean ± std. dev. of 7 runs, 1000 loops each)
## 9.13 ms ± 1.1 ms per loop (mean ± std. dev. of 7 runs, 100 loops each)
## 8.72 ms ± 789 µs per loop (mean ± std. dev. of 7 runs, 100 loops each)
## 230 ms ± 58.9 ms per loop (mean ± std. dev. of 7 runs, 1 loop each)
## 72.8 ms ± 7.94 ms per loop (mean ± std. dev. of 7 runs, 10 loops each)
## 47.6 ms ± 6.82 ms per loop (mean ± std. dev. of 7 runs, 10 loops each)


# %timeit sudoku_solver(sudoku_evil3)
## The slowest run took 4.75 times longer than the fastest. This could mean that an intermediate result is being cached.
## 5min 43s ± 4min 40s per loop (mean ± std. dev. of 7 runs, 1 loop each)

# %timeit sudoku_solver(sudoku_evil3_2)
## 12 s ± 345 ms per loop (mean ± std. dev. of 7 runs, 1 loop each)



#%% Timeit sudoku_solver_backtrack


