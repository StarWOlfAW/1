import pytest
from Homework8.sort import quick


@pytest.mark.parametrize(
    ('list', 'outcome'),
    [
        ([4, 2, 6, 1, 5, 3], [1, 2, 3, 4, 5, 6]),
        ([9, 8, 7, 6, 5, 4, 3, 2, 1], [1, 2, 3, 4, 5, 6, 7, 8, 9]),
        ([68, 54, 12, 333,], [12, 54, 68, 333]),
        ([], []),
        ([1], [1])
    ]
)
def test(list, outcome):
    assert quick(list) == outcome