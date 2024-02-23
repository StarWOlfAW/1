import pytest
from fract.Fractions import Fraction

@pytest.mark.parametrize(
    ('numer', 'denom'),
    [
        (2, 2)
    ]
)
def init(numer, denom):
    f = Fraction(numer, denom)
    assert f.numer == numer
    assert f.denom == denom
    s1 = Fraction()
    assert s1.numer == 1
    assert s1.denom == 1
def input(mocker):
    mocker.patch('builtins.input', side_effect = ['2', '2'])
    fra = Fraction()
    fra.input()
    assert fra.numer == 2
    assert fra.denom == 2

@pytest.mark.parametrize(
    ('numer', 'denom', 'output'),
    [
        (2, 1, '2/1'),
        (2, 0, '2/0')
    ]
)
def out(numer, denom, output):
    assert Fraction.__str__(Fraction(numer, denom)) == output