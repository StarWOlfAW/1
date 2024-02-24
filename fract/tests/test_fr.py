import pytest
from fract.Fractions import Fraction


def test_init():
    s1 = Fraction()
    assert s1.numer == 1
    assert s1.denom == 1
def test_input(mocker):
    mocker.patch('builtins.input', side_effect = ['2', '2'])
    fra = Fraction()
    fra.input()
    assert fra.numer == 2
    assert fra.denom == 2

@pytest.mark.parametrize(
    ('numer', 'denom', 'output'),
    [
        (2, 1, '2/1'),
        (2, 20, '2/20'),
        (2, 0, "Деление на ноль")
    ]
)
def test_out(numer, denom, output):
    assert str(Fraction(numer, denom)) == output