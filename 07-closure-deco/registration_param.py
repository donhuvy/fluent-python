registry = set()  # Faster insertion and removal

def register(active=True):  # This is a decorator factory
    def decorate(func):  # This is the actual decorator
        print(f'running register(active={active})->decorate({func})')
        if active:
            registry.add(func)
        else:
            registry.discard(func)

        return func
    return decorate

@register(active=False)
def f1():
    print('running f1()')

@register()
def f2():
    print('running f2()')

@register(active=True)
def f3():
    print('running f3()')
