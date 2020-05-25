# Notes

* `+=` -> `__iadd__`, if not implemented, falls back to `__add__`.
* `*=` -> `__imul__`, if not implemented, falls back to `__mul__`.
* `id()`: returns the "identity" of an object, guaranteed to be unique and constant for this object during its lifetime.
* Python visualization tool: pythontutor.com.
* Putting mutable items in tuples is not a good idea.
* Python API convention: functions or methods that change an object in place should return `None` to make it clear to the caller that the object itself was changed, and no new object was created (e.g., `list.sort()` vs. `sorted(list)`).
