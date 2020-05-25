'''
For mutable sequence such as list, it is the same object
after multiplication, with new items appended.
'''

l = [1, 2, 3]
print(f"id of the list before mul: {id(l)}")

l *= 2
print(f"id of the list after mul is the same: {id(l)}")

'''
For immutable sequence such as tuple, it is NOT the same object
after multiplication, a new object is created.
'''

t = (1, 2, 3)
print(f"id of the tuple before mul: {id(t)}")

t *= 2
print(f"id of the tuple after mul is NOT the same: {id(t)}")