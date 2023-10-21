from Homework4.ex3 import notsame


def test():
    assert notsame([True, 1]) == True
    assert notsame([1, 1, 2]) == False