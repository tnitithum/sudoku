# Sudoku Solver

This Sudoku solver uses a reduction method instead of the backtracking method.
Some assumptions when utilising this Sudoku solver are:

* Sudoku is valid.
* Sudoku has a unique solution.
* Input of Sudoku is `np.array` with shape of `(K**2,K**2)` where `K` is an integer such that `K>=2`. 

In other words, it's not limited to the traditional 9 by 9 Sudoku grid,
so long the numbers in the grid:

* Span from `1` to `K**2`,
* Represents missing cells as `0`.


## Method

This implements a reduction method by iteratively removing impossible clues, then fills in cells that only have one clue remaining.
If no cells are filled in that iteration, then the algorithm starts guessing by filling in cells <!-- with the lowest number of clues  -->
and creates a list of Sudoku grids with each element of the list representing a guess.
The iteration continues until it encounters a solved Sudoku grid.
If it encounters a cell with no possible clues, it removes that grid from the list and continues the iteration as usual.


## Examples

Here is an example using the 
[World's hardest sudoku: can you crack it?](https://www.telegraph.co.uk/news/science/science-news/9359579/Worlds-hardest-sudoku-can-you-crack-it.html),
which takes about 12 seconds to run.

```python
import numpy as np
from sudoku_solver import sudoku_solver
_ = 0

sudoku_hardest3 = np.array([
    [8, _, _, _, _, _, _, _, _],
    [_, _, 3, 6, _, _, _, _, _],
    [_, 7, _, _, 9, _, 2, _, _],
    [_, 5, _, _, _, 7, _, _, _],
    [_, _, _, _, 4, 5, 7, _, _],
    [_, _, _, 1, _, _, _, 3, _],
    [_, _, 1, _, _, _, _, 6, 8],
    [_, _, 8, 5, _, _, _, 1, _],
    [_, 9, _, _, _, _, 4, _, _]])
sudoku_solver(sudoku_hardest3)
# array([[8, 1, 2, 7, 5, 3, 6, 4, 9],
#        [9, 4, 3, 6, 8, 2, 1, 7, 5],
#        [6, 7, 5, 4, 9, 1, 2, 8, 3],
#        [1, 5, 4, 2, 3, 7, 8, 9, 6],
#        [3, 6, 9, 8, 4, 5, 7, 2, 1],
#        [2, 8, 7, 1, 6, 9, 5, 3, 4],
#        [5, 2, 1, 9, 7, 4, 3, 6, 8],
#        [4, 3, 8, 5, 2, 6, 9, 1, 7],
#        [7, 9, 6, 3, 1, 8, 4, 5, 2]])
```
