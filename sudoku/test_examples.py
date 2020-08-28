import numpy as np
import unittest
from sudoku_solver import sudoku_solver
from sudoku_examples import *

class TestExamples(unittest.TestCase):

    def test_easy2(self):
        self.assertTrue(np.all(sudoku_solver(sudoku_easy2) == sudoku_easy2_solution))

    def test_easy3(self):
        self.assertTrue(np.all(sudoku_solver(sudoku_easy3) == sudoku_easy3_solution))

    def test_medium3(self):
        self.assertTrue(np.all(sudoku_solver(sudoku_medium3) == sudoku_medium3_solution))


    def test_hard3(self):
        self.assertTrue(np.all(sudoku_solver(sudoku_hard3) == sudoku_hard3_solution))

    def test_expert3(self):
        self.assertTrue(np.all(sudoku_solver(sudoku_expert3) == sudoku_expert3_solution))

if __name__ == '__main__':
    unittest.main()
