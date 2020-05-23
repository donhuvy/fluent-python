# Notes

## `__repr__` vs `__str__`

* `__repr__` is for developers, use `%r`, to be unambiguous.
* `__str__` is for customers, use `%s`, to be readable.
* If `__repr__` is defined, and `__str__` is not, the object will behave as though `__str__` = `__repr__`.
* [reference](https://stackoverflow.com/questions/1436703/difference-between-str-and-repr)

### Example:
```
>>> import datetime
>>> today = datetime.datetime.now()
>>> print(today)
2020-05-23 13:57:57.803144
>>> str(today)
'2020-05-23 13:57:57.803144'
>>> repr(today)
'datetime.datetime(2020, 5, 23, 13, 57, 57, 803144)'
```