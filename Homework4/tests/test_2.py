import pytest
from Homework4.ex2 import cn


@pytest.mark.parametrize(
    ('n', 'end'),
    [
        (5, 120),
        (4, 24),
        (0, 1)
    ]
)
def test(n, end):
    assert cn(n) == end
