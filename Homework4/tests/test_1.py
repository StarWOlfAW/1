from Homework4.ex14 import swap


def test():
    assert swap([1, 2, 3, 4, 5], 2) == [4, 5, 1, 2, 3]
    assert swap([1, 2, 3, 4, 5], 3) == [3, 4, 5, 1, 2]