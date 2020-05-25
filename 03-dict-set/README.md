# Notes

* Since Python 3.6, `dict` is insertion ordered, same as `collections.OrderedDict`.
* `collections.defaultdict` provides default values to the non-existing keys, instead of raising a `KeyError` for a normal `dict`. A `default_factory` method could be provided to instantiate the `defaultdict` to customerize the default behavior.
