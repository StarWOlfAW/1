import pytest
from Homework5.ex1 import find_bin


@pytest.mark.parametrize(
    ('place', 'num', 'mid'),
    [
        (list(map(float, [1, 2, 3, 4, 5])), 4.0, 3),
        (list(map(float, [1, 2, 3, 4, 5])), 6.0, "NaN"),
        (list(map(float, [1, 2, 3, 4, 5, 6, 7, 8, 9, 10])), 3.0, 2),
        (list(map(float, [1, 2, 3, 4, 5, 6, 7, 8, 9, 10])), 4.0, 3),
        (list(map(float, [1, 2, 3, 4, 5, 6, 7, 8, 9, 10])), 1.0, 0),
        (list(map(float, [1, 2, 3, 4, 5, 6, 7, 8, 9, 10])), -1.0, "NaN"),
        (list(map(float, [2, 3, 4, 4, 4, 5, 6])), 4.0, 3),
        (list(map(float, [1, 1, 2, 2, 3, 3, 3, 27, 28, 56])), 2.0, 2),
        (list(map(float, [56, 230, 234, 747, 83274, 823573723])), 823573723.0, 5),
        (list(map(float, [1])), 1.0, 0),
    ]
)
def test(place, num, mid):
    assert find_bin(place, num) == mid
