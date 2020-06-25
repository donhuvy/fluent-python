# Notes

* [The definitive guide on how to use static, class or abstract methods in Python](https://julien.danjou.info/guide-python-static-class-abstract-methods/)

* `__slots__`:
  * Python stores instance attributes in a per-instance dict named `__dict__`. Dictionaries have a significant memory overhead because of the underlying hash table used to provide fast access. The `__slots__` class attribute can save a lot of memory by letting the interpreter store the instance attributes in a tuple instead of a dict.
  * Problems:
    * Need to reclare in each subclass, because the inherited attribute is ignored by the interpreter.
    * Instances will only be able to have the attributes listed in `__slots__`, unless you include `__dict__` in `__slots__` which defeat its purporse.
    * Instances cannot be targets of weak references unless you remember to include `__weakref__` in `__slots__`.
  * Use `numpy` for numerical data and `pandas` for large amount of data, which already taking care of memory optimization.