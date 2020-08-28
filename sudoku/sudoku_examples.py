import numpy as np

_ = 0

sudoku_easy2 = np.array([
    [_, _, 1, _],
    [2, _, _, _],
    [_, _, _, 3],
    [_, 3, _, _]])
sudoku_easy2_solution = np.array([
    [3, 4, 1, 2],
    [2, 1, 3, 4],
    [1, 2, 4, 3],
    [4, 3, 2, 1]])

sudoku_easy3 = np.array([
    [_, _, _, _, 5, _, 1, _, 7],
    [9, _, _, _, 8, 6, 3, 4, _],
    [4, 2, 7, _, _, 9, _, 6, 8],
    [_, _, 8, 2, 6, _, _, _, _],
    [7, 6, 4, _, 3, _, 2, _, 9],
    [_, 3, 2, _, _, 4, 6, 8, _],
    [8, 7, 1, _, _, _, _, _, _],
    [_, _, _, _, _, _, _, 5, 1],
    [2, _, _, _, _, 8, 4, 7, 3]])
sudoku_easy3_solution = np.array([
    [6, 8, 3, 4, 5, 2, 1, 9, 7],
    [9, 1, 5, 7, 8, 6, 3, 4, 2],
    [4, 2, 7, 3, 1, 9, 5, 6, 8],
    [5, 9, 8, 2, 6, 1, 7, 3, 4],
    [7, 6, 4, 8, 3, 5, 2, 1, 9],
    [1, 3, 2, 9, 7, 4, 6, 8, 5],
    [8, 7, 1, 5, 4, 3, 9, 2, 6],
    [3, 4, 9, 6, 2, 7, 8, 5, 1],
    [2, 5, 6, 1, 9, 8, 4, 7, 3]])

sudoku_medium3 = np.array([
    [_, _, _, 3, 4, _, _, _, 1],
    [_, 5, _, _, 2, 6, _, _, _],
    [_, _, _, _, _, _, 2, _, _],
    [_, _, 5, _, _, _, 1, _, 2],
    [_, _, 4, _, 6, 2, 5, 9, 8],
    [_, _, _, 5, _, _, _, _, 4],
    [_, 6, 8, _, 1, _, _, _, _],
    [3, _, 2, _, 8, _, 9, 1, _],
    [_, 9, 7, _, _, _, 6, _, 3]])
sudoku_medium3_solution = np.array([
    [9, 2, 6, 3, 4, 5, 8, 7, 1],
    [8, 5, 1, 7, 2, 6, 3, 4, 9],
    [4, 7, 3, 8, 9, 1, 2, 5, 6],
    [6, 8, 5, 4, 7, 9, 1, 3, 2],
    [7, 3, 4, 1, 6, 2, 5, 9, 8],
    [2, 1, 9, 5, 3, 8, 7, 6, 4],
    [5, 6, 8, 9, 1, 3, 4, 2, 7],
    [3, 4, 2, 6, 8, 7, 9, 1, 5],
    [1, 9, 7, 2, 5, 4, 6, 8, 3]])

sudoku_hard3 = np.array([
    [7, _, _, 5, 6, _, _, _, _],
    [5, _, 1, _, _, _, _, _, _],
    [_, _, _, _, _, _, 2, _, 4],
    [_, _, 3, _, _, _, _, 7, _],
    [_, _, _, _, 3, _, 1, _, _],
    [4, _, 6, 2, 1, 9, _, _, _],
    [6, _, 5, _, _, 3, _, _, 1],
    [_, _, _, 8, _, _, _, 2, 6],
    [_, 8, _, 9, _, _, _, _, _]])
sudoku_hard3_solution = np.array([
    [7, 4, 2, 5, 6, 8, 9, 1, 3],
    [5, 9, 1, 3, 4, 2, 6, 8, 7],
    [3, 6, 8, 1, 9, 7, 2, 5, 4],
    [2, 1, 3, 6, 8, 5, 4, 7, 9],
    [8, 5, 9, 7, 3, 4, 1, 6, 2],
    [4, 7, 6, 2, 1, 9, 5, 3, 8],
    [6, 2, 5, 4, 7, 3, 8, 9, 1],
    [9, 3, 4, 8, 5, 1, 7, 2, 6],
    [1, 8, 7, 9, 2, 6, 3, 4, 5]]) 

sudoku_expert3 = np.array([
    [_, _, _, 9, _, _, _, _, 7],
    [_, _, _, 8, _, 1, _, 9, _],
    [8, _, 1, 4, _, _, _, _, _],
    [9, _, _, 5, _, 8, 4, _, _],
    [_, _, 4, _, _, _, _, 3, _],
    [_, _, 7, _, _, _, 9, _, _],
    [_, _, _, 6, _, _, _, _, 3],
    [1, _, 2, _, 3, 4, _, _, _],
    [5, _, _, _, _, _, _, _, _]])
sudoku_expert3_solution = np.array([
    [3, 4, 5, 9, 2, 6, 8, 1, 7],
    [7, 2, 6, 8, 5, 1, 3, 9, 4],
    [8, 9, 1, 4, 7, 3, 2, 6, 5],
    [9, 1, 3, 5, 6, 8, 4, 7, 2],
    [2, 5, 4, 1, 9, 7, 6, 3, 8],
    [6, 8, 7, 3, 4, 2, 9, 5, 1],
    [4, 7, 9, 6, 8, 5, 1, 2, 3],
    [1, 6, 2, 7, 3, 4, 5, 8, 9],
    [5, 3, 8, 2, 1, 9, 7, 4, 6]])

sudoku_evil3 = np.array([   # 17 clue puzzle
    [_, _, _, _, _, _, _, 4, 1],
    [_, _, 9, 3, _, _, _, _, _],
    [_, _, _, _, _, _, 5, 2, _],
    [_, _, _, 8, _, _, 3, _, _],
    [4, 2, _, _, _, _, _, _, _],
    [5, _, _, _, _, _, _, _, 7],
    [_, 6, _, _, _, 4, 2, _, _],
    [_, _, _, _, 1, _, _, _, _],
    [_, _, 8, _, _, _, _, _, _]])

#https://www.telegraph.co.uk/news/science/science-news/9359579/Worlds-hardest-sudoku-can-you-crack-it.html
sudoku_hardest3 = np.array([   # 17 clue puzzle
    [8, _, _, _, _, _, _, _, _],
    [_, _, 3, 6, _, _, _, _, _],
    [_, 7, _, _, 9, _, 2, _, _],
    [_, 5, _, _, _, 7, _, _, _],
    [_, _, _, _, 4, 5, 7, _, _],
    [_, _, _, 1, _, _, _, 3, _],
    [_, _, 1, _, _, _, _, 6, 8],
    [_, _, 8, 5, _, _, _, 1, _],
    [_, 9, _, _, _, _, 4, _, _]])


sudoku_16x16_beginner_1 = np.array([
    [12,  _,  7,  8,  _,  5, 15,  _,  3,  _,  _, 11, 14,  _, 13, 10],
    [ _,  _,  4,  _,  _,  7,  _,  _,  _, 13,  _, 16, 11,  _,  _,  2],
    [11,  _,  _,  _,  _,  _,  _,  _,  _,  _,  _,  4,  3,  7,  _,  _],
    [ _,  _,  5,  _,  _,  _,  9, 16,  _,  _,  _,  _,  _,  _,  _,  8],
    [ _,  4,  _,  _, 12,  8,  _,  _,  _, 15,  _,  7,  9,  3,  _,  _],
    [ _,  _, 15,  3,  7, 13,  _,  _,  _,  _, 16, 14, 12,  _,  _,  4],
    [ 9, 16,  _,  7,  _,  _,  5, 14,  _,  3,  _,  _,  _,  _,  8,  _],
    [ 5,  _,  _, 14,  _, 16,  3,  _,  2,  4, 11,  8, 13,  _, 10,  _],
    [ _,  8,  _,  _,  _,  _,  _,  _, 12,  _,  _,  _,  _, 10, 14,  5],
    [ _,  _, 14,  _,  _,  _,  _,  _,  _,  8,  _,  _, 16,  _, 15,  _],
    [ _,  _, 11,  _,  9,  _, 16,  _,  _,  6,  7,  _,  _,  _, 12, 13],
    [ _,  _,  _, 13,  _, 11, 12,  _,  _,  _,  _, 15,  7,  2,  4,  _],
    [ 7, 11,  _,  9,  _, 12,  1,  _,  _,  _,  5,  _,  _,  6,  3,  _],
    [14,  _, 13, 15, 16,  _,  7,  _, 11,  _,  _,  _,  _,  8,  _,  _],
    [ _,  _,  _,  _, 15,  _, 11,  _,  _, 14,  _,  _,  5,  _,  _,  _],
    [ _,  6,  3,  5, 10,  9, 13,  _,  _, 12,  _,  _, 15,  _,  _,  _]])


sudoku_16x16_confirmed_1 = np.array([
[ _,  _,  _,  _,  _,  5,  _,  _,  6,  _, 16,  _, 12,  _,  4,  _],
[ _,  _,  4,  9,  _, 15, 11,  _,  8,  3,  _,  _, 14,  _,  _,  _],
[ _,  _, 15,  6,  8, 10, 14,  _,  _, 12,  _,  _,  _, 16,  _,  _],
[ _,  _,  _,  _,  1,  _,  _,  _,  _, 14,  4, 11,  _,  8,  3,  6],
[ _,  _,  _,  8,  _,  1,  7,  _,  _,  4,  2,  3,  _,  _, 11, 14],
[ _,  _,  _,  _, 10,  _,  _, 15, 14, 11,  _,  _,  _,  _,  _,  _],
[ _, 15,  5,  2, 14,  6,  4,  _,  _,  1,  _,  9,  _, 13, 10,  _],
[ _,  _,  _,  _,  _,  _,  2,  _,  _,  _, 12,  _,  _,  9, 15,  _],
[ _,  _,  _,  _, 15, 14, 12,  1,  _,  8, 13,  _,  5,  _,  _,  _],
[ _,  _,  _, 15,  3,  _,  _,  _,  _,  _,  _,  _,  7,  _,  2,  9],
[ _,  _,  _,  _,  _,  _,  _,  _,  _,  _,  _,  7,  3,  _, 13, 16],
[ 6,  _,  _,  _,  _, 16,  _,  _,  5,  _,  _, 14,  _, 12,  _,  _],
[ _,  _,  _,  _,  5,  _,  _, 16,  _,  _,  _,  2,  _,  _,  1, 15],
[ 8,  _,  _, 10,  _,  _,  _,  _,  _,  _,  _,  _, 13,  2,  _,  _],
[ _,  5,  6, 11,  _,  _, 10,  _,  3,  _,  1,  4,  _,  7,  _,  _],
[ _,  3,  1,  _,  9,  _,  _,  _, 16,  _,  7,  _, 10,  _,  5,  _]])

sudoku_16x16_confirmed_1000 = np.array([
    [ _,  _,  _,  _,  _,  _,  _,  4,  3,  _, 16,  _,  _,  6, 14,  _],
    [ _, 16,  _,  8,  _,  _,  3,  _,  _,  _,  _,  6, 12,  _,  2,  _],
    [ _, 11, 15,  _,  _, 13,  _,  _,  _, 12,  4,  _,  _,  _,  _,  _],
    [13,  _,  _,  _,  _,  _,  9,  _,  _, 15,  _,  _,  7, 10,  3,  _],
    [ _,  _,  _,  _,  _,  _, 12, 13, 14,  _,  _,  _,  _,  _,  _,  _],
    [ _,  4,  _,  _,  _,  8,  _,  _, 11, 16, 15,  _,  _, 12,  _,  _],
    [15,  _,  _,  _,  _,  _,  _,  _,  7,  6,  8,  _,  _,  _, 16,  _],
    [ 6,  _,  8,  _,  4, 10, 11, 14,  _,  _,  _, 13,  _, 15,  _,  _],
    [ _,  8,  _,  2,  _,  9,  _,  _,  _,  _,  _,  4, 14,  _,  7,  _],
    [ _,  3,  _,  _,  _,  _,  _, 12,  2,  _, 14, 10,  5,  4,  _,  _],
    [11, 12,  _,  1, 13,  _, 15,  _,  _,  9,  _,  _, 16,  _,  _,  _],
    [ _,  _,  _,  _,  _,  _, 16,  _,  _,  _,  _,  7,  _,  _,  _,  _],
    [ _, 15, 13, 14, 11,  _,  _,  _,  _,  _,  9,  _,  _, 16,  _,  _],
    [ 4,  _,  _,  5,  _,  7,  _, 15, 13,  _,  _,  3,  _,  _,  _,  _],
    [16,  _,  3,  _, 12,  _,  _,  _,  _,  _,  _,  _,  8,  9,  _,  2],
    [ _,  _,  _, 11,  _, 14, 13,  _,  _,  _,  _,  _,  _,  1,  _,  _]])