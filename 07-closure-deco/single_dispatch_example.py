import html
import numbers
from collections import abc
from functools import singledispatch


@singledispatch  # Marks the base function
def htmlize(obj):
    content = html.escape(repr(obj))
    return f'<pre>{content}</pre>'

@htmlize.register(str)  # Register the specialized function
def _(text):  # Name is irrelevant
    content = html.escape(text).replace('\n', '<br>\n')
    return f'<p>{content}</p>'

@htmlize.register(numbers.Integral)  # Virtual superclass of int
def _(n):
    return '<pre>{0} (0x{0:x})</pre>'.format(n)

@htmlize.register(tuple)  # Can also stack the registrations
@htmlize.register(abc.MutableSequence)
def _(seq):
    inner = '</li>\n<li>'.join(htmlize(item) for item in seq)
    return '<ul>\n<li>' + inner + '</li>\n</ul>'

if __name__ == '__main__':
    assert htmlize({1, 2, 3}) == '<pre>{1, 2, 3}</pre>'
    assert htmlize(42)  == '<pre>42 (0x2a)</pre>'
