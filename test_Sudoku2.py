import pytest
from sudoku import*

def test_convertToSets():
    array = [[0, 1, 2], [1, 0, 2], [0, 1, 0]]
    zero = set(range(1, 10))
    new_array = [[zero, {1}, {2}], [{1}, zero, {2}], [zero, {1}, zero]]
    assert new_array == convertToSets(array)

