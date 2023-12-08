import pytest
from Homework7.ex1 import search


@pytest.mark.parametrize(
    ('gr', 'st', 'cur', 'forward'),
    [
        ({'A':[],'B':[]'C':[]}, 'A', 'C', None),
        ({'A':['B', 'C'], 'B':['A', 'D'], 'C':['A', 'D'], 'D':['B', 'C', 'E'], 'E':['D']}, 'A', 'E', 3),
        ({'A': ['B', 'C'], 'B':['D', 'F'], 'C':['D', 'E'], 'D':['E']}, 'A', 'A', 0),
    ]
)
def test(gr, st, cur, forward):
    assert search(gr, st, cur) == forward
