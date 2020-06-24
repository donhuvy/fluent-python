# List
l1 = [1, 2, 3]
l2 = l1
assert l2 is l1
l3 = list(l1)  # Make a copy
assert l3 == l1
assert l3 is not l1
l4 = l1[:]  # Make a copy
assert l4 == l1
assert l4 is not l1

# Tuple
t1 = (1, 2, 3)
t2 = tuple(t1)  #  Not making a copy
assert t2 is t1
t3 = t1[:]  #  Not making a copy
assert t3 is t1
t4 = (1, 2, 3)
assert t4 == t1
assert t4 is t1  # hmm...

# Str
s1 = 'abc'
s2 = 'abc'
assert s2 == s1
assert s2 is s1

'''
The sharing of string literals is an optimization technique
called interning, similar for int
'''

# int
i1 = 42
i2 = 42
assert i2 == i1
assert i2 is i1

'''
However, alwasy use == and not is to compare string and int
for equality. Interning is a feature for internal use of the
Python interpreter.
'''
