import pytest # type: ignore
from averager import make_averager


def test_averager():
    avg = make_averager()
    assert avg(10) == 10.0
    assert avg(11) == 10.5
    assert avg(12) == 11.0
    
    assert avg.__code__.co_freevars == ('series',)
    assert avg.__closure__[0].cell_contents == [10, 11, 12]


if __name__ == '__main__':
    pytest.main()
