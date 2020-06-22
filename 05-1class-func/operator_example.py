from functools import reduce
from operator import mul

def fact1(n: int) -> int:
    return reduce(lambda a, b: a*b, range(1, n+1))

def fact2(n: int) -> int:
    return reduce(mul, range(1, n+1))

if __name__ == "__main__":
    assert fact1(5) == fact2(5) == 120