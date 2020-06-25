from array import array
import math


class Vector2d:
    __slots__ = ('__x', '__y')

    typecode = 'd'  # d for float

    def __init__(self, x, y):
        # Two leading underscores for private
        self.__x = float(x)
        self.__y = float(y)

    @property
    def x(self):
        '''
        Use property decorator to mark as read-only,
        used for implementing __hash__ which takes
        inmmutable keys only.
        '''
        return self.__x
    
    @property
    def y(self):
        return self.__y

    def __hash__(self):
        return hash(self.x) ^ hash(self.y)

    def __iter__(self):
        '''
        Makes it iterable, which makes the unpacking work
        (e.g., x, y = my_vector). could also be:
        yield self.x; yield self.y;
        '''
        return (i for i in (self.x, self.y))

    def __repr__(self):
        class_name = type(self).__name__
        return '{}({!r}, {!r})'.format(class_name, *self)

    def __str__(self):
        return str(tuple(self))

    def __bytes__(self):
        return (bytes([ord(self.typecode)]) +
                bytes(array(self.typecode, self)))

    def __eq__(self, other):
        return tuple(self) == tuple(other)

    def __abs__(self):
        return math.hypot(self.x, self.y)

    def __bool__(self):
        return bool(abs(self))

    def angle(self):
        return math.atan2(self.y, self.x)

    def __format__(self, fmt_spec=''):
        # Choose p as it is not already a format specifier 
        if fmt_spec.endswith('p'):
            fmt_spec = fmt_spec[:-1]
            coords = (abs(self), self.angle())
            outer_fmt = '<{}, {}>'
        else:
            coords = self
            outer_fmt = '({}, {})'
        components = (format(c, fmt_spec) for c in coords)
        return outer_fmt.format(*components)

    @classmethod
    # No self as input because of classmethod
    def frombytes(cls, octets):  # Ask Google octet vs byte
        '''
        Construct a vector from a binary sequence.
        '''
        # Read a typecode from the first byte
        typecode = chr(octets[0])
        # Create a memory view of the binary sequence and
        # cast with the typecode
        memv = memoryview(octets[1:]).cast(typecode)
        # Unpack the result and use it for the constructor
        return cls(*memv)

if __name__ == '__main__':
    v1 = Vector2d(3, 4)
    x, y = v1
    assert x == 3.0
    assert y == 4.0
    assert repr(v1) == 'Vector2d(3.0, 4.0)'
    
    v1_clone = eval(repr(v1))
    assert v1_clone == v1

    assert abs(v1) == 5.0
    assert bool(v1) is True
    assert bool(Vector2d(0, 0)) is False

    print(tuple(v1))
    print(str(v1))
    print(bytes(v1))

    v2 = Vector2d.frombytes(bytes(v1))
    assert v2 == v1
    
    assert format(v1, '.2f') == '(3.00, 4.00)'
    assert format(v1, '.3e') == '(3.000e+00, 4.000e+00)'
    assert format(Vector2d(1, 1), '.5fp') == '<1.41421, 0.78540>'

    print(hash(v1))
    assert hash(v1_clone) == hash(v1)

    # RIP
    assert hash(Vector2d(3,4)) == hash(Vector2d(4, 3))
    