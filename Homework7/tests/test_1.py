import pytest
from Homework7.ex1 import search


def condition(this, cur):
    return this == cur


def cc(this, cur):
    return this[0] == 'A'


@pytest.mark.parametrize(
    ('gr', 'st', 'cur', 'forward', 'f'),
    [
        ({'A': [], 'B': [], 'C': []}, 'A', 'C', None, condition),
        ({'A': ['B', 'C'], 'B': ['D'], 'C': ['D'], 'D': ['E'], 'E': []}, 'A', 'E', 3, condition),
        ({'A': ['B', 'C'], 'B': ['D', 'A'], 'C': ['D', 'E'], 'D': ['E']}, 'A', 'A', 0, condition),
        ({}, 'A', 'A', None, condition),
        ({'B': ['A'], 'A': []}, 'B', 'A', 1, cc)
    ]
)
def test(gr, st, cur, forward, f):
    assert search(gr, st, cur, f) == forward
