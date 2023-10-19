from Homework4.ex3 import afe


def test():
    assert afe([1, 2, 3]) == True
    assert afe([1, 1, 2]) == False