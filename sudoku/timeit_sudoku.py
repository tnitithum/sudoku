#%% Import Libraries
import numpy as np
import timeit
from sudoku_solver import sudoku_solver
from sudoku_examples import *


#%% Timeit

%timeit sudoku_solver(sudoku_easy2)

%timeit sudoku_solver(sudoku_easy3)

%timeit sudoku_solver(sudoku_medium3)

%timeit sudoku_solver(sudoku_hard3)

%timeit sudoku_solver(sudoku_expert3)

%timeit sudoku_solver(sudoku_16x16_beginner_1)

%timeit sudoku_solver(sudoku_16x16_confirmed_1)


## 1.22 ms ± 161 µs per loop (mean ± std. dev. of 7 runs, 1000 loops each)
## 8.87 ms ± 1.12 ms per loop (mean ± std. dev. of 7 runs, 100 loops each)
## 8.85 ms ± 731 µs per loop (mean ± std. dev. of 7 runs, 100 loops each)
## 235 ms ± 71.4 ms per loop (mean ± std. dev. of 7 runs, 1 loop each)
## 72 ms ± 7.29 ms per loop (mean ± std. dev. of 7 runs, 10 loops each)
## 50.4 ms ± 7.19 ms per loop (mean ± std. dev. of 7 runs, 10 loops each)
## 51.6 ms ± 2.55 ms per loop (mean ± std. dev. of 7 runs, 10 loops each)



# %timeit sudoku_solver(sudoku_evil3)
## The slowest run took 4.75 times longer than the fastest. This could mean that an intermediate result is being cached.
## 5min 43s ± 4min 40s per loop (mean ± std. dev. of 7 runs, 1 loop each)

# %timeit sudoku_solver(sudoku_hardest3)
## 12 s ± 345 ms per loop (mean ± std. dev. of 7 runs, 1 loop each)
