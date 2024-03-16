import pytest
from fract.Fractions import Fraction
from fract.Fractions import ReduceFraction


def test_init():
    s1 = Fraction()
    assert s1.numer == 1
    assert s1.denom == 1


def test_input(mocker):
    mocker.patch('builtins.input', side_effect = ['2', '2'])
    fra = Fraction()
    srt = fra.input()
    assert srt == True
    assert fra.numer == 2
    assert fra.denom == 2


@pytest.mark.parametrize(
    ('numer', 'denom', 'output'),
    [
        (2, 1, '2/1'),
        (2, 20, '2/20'),
    ]
)
def test_out(numer, denom, output):
    assert str(Fraction(numer, denom)) == output


@pytest.mark.parametrize(
    ('numer', 'denom', 'output1', 'output2'),
    [
        (10, 20, 1, 2),
        (-10, -20, -1, -2)
    ]
)
def test_reduce(numer, denom, output1, output2):
    l = Fraction(numer, denom)
    l.reduce()
    assert l.numer == output1
    assert l.denom == output2


@pytest.mark.xfail(raises = ZeroDivisionError)
def test_error():
    Fraction(1, 0)


@pytest.mark.xfail(raises = ValueError)
def test_error2(mocker):
    mocker.patch('builtins.input', side_effect = ['ty', 'sm'])
    d = Fraction()
    d.input()


@pytest.mark.parametrize(
    ('numer', 'denom', 'output'),
    [
        (0, 10, '0/1'),
        (-10, 20, '-1/2'),
        (10, -20, '1/-2')
    ]
)
def test_instant(numer, denom, output):
    assert str(ReduceFraction(numer, denom)) == output


@pytest.mark.parametrize(
    ('numer', 'denom', 'numer2', 'denom2', 'numer3', 'denom3'),
    [
        (1, 2, 1, 3, 5, 6),
        (0, 2, 1, 5, 2, 10),
        (3, 3, 1, 2, 9, 6)
    ]
)
def test_sum(numer, denom, numer2, denom2, numer3, denom3):
    assert Fraction(numer, denom) + Fraction(numer2, denom2) == Fraction(numer3, denom3)


@pytest.mark.parametrize(
    ('numer', 'denom', 'numer2', 'denom2', 'numer3', 'denom3'),
    [
        (1, 2, 1, 3, 1, 6),
        (0, 2, 1, 5, -2, 10),
        (3, 3, 1, 2, 3, 6)
    ]
)
def test_sub(numer, denom, numer2, denom2, numer3, denom3):
    assert Fraction(numer, denom) - Fraction(numer2, denom2) == Fraction(numer3, denom3)


@pytest.mark.parametrize(
    ('numer', 'denom', 'numer2', 'denom2', 'numer3', 'denom3'),
    [
        (1, 2, 1, 3, 1, 6),
        (0, 2, 1, 5, -1, 5),
        (3, 3, 1, 2, 1, 2)
    ]
)
def test_redsub(numer, denom, numer2, denom2, numer3, denom3):
    assert ReduceFraction(numer, denom) - Fraction(numer2, denom2) == Fraction(numer3, denom3)