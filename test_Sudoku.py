import pytest
from sudoku import*


def test_ConvertToSets():
    array = [[0, 1, 2], [1, 0, 2], [0, 1, 0]]
    zero = set(range(1, 10))
    new_array = [[zero, {1}, {2}], [{1}, zero, {2}], [zero, {1}, zero]]
    assert type(array[0][0]) == int
    assert new_array == convertToSets(array)


def test_ConvertToInts():
    sets = [[{1, 2}, {3}, {4}], [{1}, {3, 5, 7}, {2}], [{2, 3}, {2}, {3}]]
    new_array2 = [[0 , 3, 4], [1, 0, 2], [0, 2, 3]]
    assert new_array2 == convertToInts(sets)
    assert type(array[0][0]) == set

def test_GetRowLocations():
    row_3 = [(3, 0), (3, 1), (3, 2), (3, 3), (3, 4), (3, 5), (3, 6), (3, 7), (3, 8)]
    assert row_3 == getRowLocations(3)


def test_GetColumnLocations():
    column_3 = [(0, 3), (1, 3), (2, 3), (3, 3), (4, 3), (5, 3), (6, 3), (7, 3), (8,3)]
    assert column_3 == getColumnLocations(3)


def test_GetBoxLocation():
    box_2 = [(0, 3), (0, 4), (0, 5), (1, 3), (1, 4), (1, 5), (2, 3), (2, 4), (2, 5)]
    assert box_2 == getBoxLocation((0,4))


def test_Eliminate():
    sets = [[{1, 2}, {3}, {4}], [{1}, {3, 5, 7}, {2}], [{2, 3}, {2}, {1, 2, 3}]]
    location = (1, 2) # contains {2}
    count = eliminate(sets, location, [(0, 0), (1, 0), (2, 2)])
    assert 2 == count
    assert sets == [[{1}, {3}, {4}], [{1}, {3, 5, 7}, {2}], [{2, 3}, {2}, {1, 3}]]


def test_IsSolved():
    array = [[{1}] * 9] * 9
    assert all([len(array[r][c]) == 1 for r in range(0, 9) for c in range(0, 9)])
    assert isSolved(array) == True

    array[3][5] = {1, 2}
    assert all([len(array[r][c]) == 1 for r in range(0, 9) for c in range(0, 9)])
    assert isSolved(array) == False


def test_Solve():
    # Easy
        sudoku1 = [[4, 0, 0,  0, 0, 3,  0, 7, 0],
                   [0, 0, 1,  0, 0, 9,  5, 0, 8],
                   [0, 0, 0,  6, 0, 8,  4, 1, 3],

                   [0, 1, 0,  9, 0, 0,  3, 0, 0],
                   [0, 0, 0,  0, 5, 0,  0, 0, 0],
                   [0, 0, 4,  0, 0, 6,  0, 8, 0],

                   [7, 9, 2,  8, 0, 5,  0, 0, 0],
                   [3, 0, 5,  4, 0, 0,  9, 0, 0],
                   [0, 4, 0,  2, 0, 0,  8, 0, 5]]
                   
        solved1 = [[4, 6, 8,  5, 1, 3,  2, 7, 9], 
                   [2, 3, 1,  7, 4, 9,  5, 6, 8], 
                   [5, 7, 9,  6, 2, 8,  4, 1, 3], 

                   [6, 1, 7,  9, 8, 2,  3, 5, 4], 
                   [8, 2, 3,  1, 5, 4,  7, 9, 6], 
                   [9, 5, 4,  3, 7, 6,  1, 8, 2], 

                   [7, 9, 2,  8, 3, 5,  6, 4, 1], 
                   [3, 8, 5,  4, 6, 1,  9, 2, 7], 
                   [1, 4, 6,  2, 9, 7,  8, 3, 5]]
        # Easy
        sudoku2 = [[0, 0, 0,  7, 0, 0,  6, 8, 9],
                   [3, 0, 8,  0, 0, 0,  2, 0, 0],
                   [0, 0, 0,  8, 1, 0,  0, 4, 0],

                   [6, 0, 0,  0, 0, 0,  8, 0, 4],
                   [8, 0, 0,  3, 4, 9,  0, 0, 5],
                   [7, 0, 5,  0, 0, 0,  0, 0, 3],

                   [0, 8, 0,  0, 7, 6,  0, 0, 0],
                   [0, 0, 7,  0, 0, 0,  1, 0, 8],
                   [9, 5, 1,  0, 0, 8,  0, 0, 0]]
                   
        solved2 = [[1, 2, 4,  7, 5, 3,  6, 8, 9],
                   [3, 7, 8,  9, 6, 4,  2, 5, 1],
                   [5, 9, 6,  8, 1, 2,  3, 4, 7],

                   [6, 3, 9,  5, 2, 7,  8, 1, 4],
                   [8, 1, 2,  3, 4, 9,  7, 6, 5],
                   [7, 4, 5,  6, 8, 1,  9, 2, 3],

                   [4, 8, 3,  1, 7, 6,  5, 9, 2],
                   [2, 6, 7,  4, 9, 5,  1, 3, 8],
                   [9, 5, 1,  2, 3, 8,  4, 7, 6]]

    tryToSolve(sudoku1, solved1)
    tryToSolve(sudoku2, solved2)


def tryToSolve(problem, solution):
    problemAsSets = convertToSets(problem)
    solved = convertToInts(problemAsSets)
    assert solution == solved
