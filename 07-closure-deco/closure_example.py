from typing import Callable

def make_multiplier_of(n: int) -> Callable:

    def multiplier(x: int) -> int:
        return x * n

    return multiplier


if __name__ == '__main__':

    times3 = make_multiplier_of(3)

    times5 = make_multiplier_of(5)

    assert times3(9) == 27

    assert times5(3) == 15

    assert times5(times3(2)) == 30
