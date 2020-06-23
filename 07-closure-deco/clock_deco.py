import time


def clock(func):

    def clocked(*args):
        t0 = time.time()
        # func is a free variable here
        result = func(*args)
        elapsed = time.time() - t0
        name = func.__name__
        arg_str = ', '.join(repr(arg) for arg in args)
        print(f'[{elapsed:0.8f}s] {name}({arg_str}) -> {result}')
        return result

    return clocked
