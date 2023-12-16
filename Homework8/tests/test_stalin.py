import pytest
from Homework8.sort import stalin


@pytest.mark.parametrize(
    ('list', 'outcome'),
    [
        ([4, 2, 6, 1, 5, 3], [4, 6]),
        ([9, 8, 7, 6, 5, 4, 3, 2, 1], [9]),
        ([68, 54, 12, 333,], [68, 333]),
        ([], []),
        ([1], [1])
    ]
)
def test(list, outcome):
    assert Stalin(list) == outcome
