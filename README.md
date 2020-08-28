# Sudoku Solver

This Sudoku solver uses a reduction method instead of the back-tracking method.
Some assumptions when utilising this Sudoku solver are:

* Sudoku is valid.
* Sudoku has a unique solution.
* Input of Sudoku is `np.array` with shape of `(K**2,K**2)` where `K` is an integer such that `K>=2`. 

In other words, it's not limited to the traditional 9 by 9 Sudoku grid,
So long the numbers in the grid:

* Span from `1` to `K**2`,
* Represents missing cells as `0`.


## Method

This implements a reduction method by iteratively removing impossible clues, then fills in cells that only have one clue remaining.
If no cells are filled in that iteration, then the algorithm starts guessing by filling in cells with the lowest number of clues and creates a list of Sudoku grids for each guess.
The iteration continues until it encounters a solved Sudoku grid.
If it encounters a cell with no possible clues, it removes that grid from the list and continues the iteration as usual.


## Examples

```python
import random

class CardGame(object):
    """ a sample python class """
    NB_CARDS = 32
    def __init__(self, cards=5):
        self.cards = random.sample(range(self.NB_CARDS), 5)
        print 'ready to play'
```



This is a simple example package. You can use
[Github-flavored Markdown](https://guides.github.com/features/mastering-markdown/)
to write your content.
