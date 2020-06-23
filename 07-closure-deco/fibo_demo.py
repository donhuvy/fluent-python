import functools
from clock_deco import clock


@clock
def fibonacci(n):
    if n < 2:
        return n
    return fibonacci(n-2) + fibonacci(n-1)


@functools.lru_cache() # parenthesis because it could take arguments
@clock
def fibonacci_lru(n):
    if n < 2:
        return n
    return fibonacci_lru(n-2) + fibonacci_lru(n-1)


if __name__=='__main__':
    print(fibonacci(6))
    print(fibonacci_lru(6))
