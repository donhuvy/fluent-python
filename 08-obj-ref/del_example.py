import weakref

# s1 and s2 are aliases to the same set
s1 = {1, 2, 3}
s2 = s1

# create a callback function to print when the
# object is destroyed
def bye():
    print('Gone with the wind...')

# register the callback function
ender = weakref.finalize(s1, bye)
assert ender.alive is True

# del deletes the name s1, not the object, the
# reference count to the object reduced from 2 to 1
del s1
assert ender.alive is True

# rebind the s2 reference, object reference count
# reduced from 1 to 0, hence object is destroyed
s2 = 'spam'  # bye() should be invoked here
assert ender.alive is not True
