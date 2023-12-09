import pytest
from Homework7.ex1 import search


@pytest.mark.parametrize(
    ('gr', 'st', 'cur', 'forward'),
    [
        ({'A': [], 'B': [], 'C': []}, 'A', 'C', None),
        ({'A': ['B', 'C'], 'B': ['D'], 'C': ['D'], 'D': ['E'], 'E': []}, 'A', 'E', 3),
        ({'A': ['B', 'C'], 'B': ['D', 'A'], 'C': ['D', 'E'], 'D': ['E']}, 'A', 'A', 0),
        ({}, 'A', 'A', None)
    ]
)
def test(gr, st, cur, forward):
    assert search(gr, st, cur) == forward
