# Notes

* Since Python 3.6, `dict` is insertion ordered, same as `collections.OrderedDict`.
* `collections.defaultdict` provides default values to the non-existing keys, instead of raising a `KeyError` for a normal `dict`. A `default_factory` method could be provided to instantiate the `defaultdict` to customerize the default behavior.
* There is an immutable `frozenset` in Python.
* Use `set` intersection is a fast and clean way to find needles in a haystack (i.e., `found = len(set(needles) & set(haystack))`).
* By default, the `__hash__` values of str and bytes objects are “salted” with an unpredictable random value. Although they remain constant within an individual Python process, they are not predictable between repeated invocations of Python.
* If you implement a class with a custom `__eq__` method and you want the instancesto be hashable, you must also implement a suitable `__hash__` to make sure that when `a == b` is `True` then `hash(a) == hash(b)` is also `True`.
* Because a `dict` uses a hash table internally, and hash tables must be sparse to work, they are not space efficient. `dict` is an example of trading space for time: dictionaries have significant memory overhead, but they provide fast acess regardless of the size of the dictionary.
