b = 6

def f1(a):
    print(a)
    print(b)
    b = 9

def f2(a):
    global b
    print(a)
    print(b)
    b = 9
    print(b)
    
if __name__ == "__main__":
    # This raises "UnboundLocalError: local variable 'b' referenced before assignment"
    f1(3)
    # This works fine
    f2(3)
