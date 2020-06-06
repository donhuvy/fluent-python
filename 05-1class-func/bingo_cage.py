import random

class BingoCage:
    def __init__(self, item):
        self._items = list(item)
        random.shuffle(self._items)
    
    def pick(self):
        try:
            return self._items.pop()
        except IndexError:
            raise LookupError("BingoCage is empty")
    
    def __call__(self):
        return self.pick()
    
if __name__ == "__main__":
    bingo = BingoCage(range(3))
    print(bingo.pick())
    print(bingo())
    print(callable(bingo))