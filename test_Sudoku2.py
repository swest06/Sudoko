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


def test_GetRowLocations():
    row_3 = [(3, 0), (3, 1), (3, 2), (3, 3), (3, 4), (3, 5), (3, 6), (3, 7), (3, 8)]
    assert row_3 == getRowLocations(3)


def test_GetColumnLocations():
    column_3 = [(0, 3), (1, 3), (2, 3), (3, 3), (4, 3), (5, 3), (6, 3), (7, 3), (8,3)]
    assert column_3 == getColumnLocations(3)


def test_GetBoxLocation():
    box_2 = [(0, 4), (0, 5), (0, 6), (1, 4), (1, 5), (1, 6), (2, 4), (2, 5), (2, 6)]
    assert box_2 == getBoxLocation((0,6))


def test_Eliminate():
    sets = [[{1, 2}, {3}, {4}], [{1}, {3, 5, 7}, {2}], [{2, 3}, {2}, {1, 2, 3}]]
    location = (1, 2) # contains {2}
    count = eliminate(sets, location, [(0, 0), (1, 0), (2, 2)])
    assert 2 == count
    assert sets == [[{1}, {3}, {4}], [{1}, {3, 5, 7}, {2}], [{2, 3}, {2}, {1, 3}]]


def test_IsSolved():
    array = [[{1}] * 9] * 9
    # TO DO
    
    
