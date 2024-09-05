from multipledispatch import dispatch

@dispatch(int, int, int)         # <-- Decorator; wraps the actual function to extend its behaviour
def add(a, b, c):
    """Adds three integers"""
    print("int addition")
    return a + b + c

@dispatch(float, float, float)
def add(a, b, c):
    """Adds three floats"""
    print("float addition")
    return a + b + c

@dispatch(int, int, int)
def add(a, b, c):
    """Adds three ints (revisited)"""
    print("Int - 2 called")
    return a + b + c


def mul(a, b):
    """
    Multiplies two values
    Usage: mul(<object>, <object>) --> <object>
    more description
    """
    return a * b


# print(add(1, 2))
print(add(1, 2, 3))
print(add(1.1, 2.2, 3.3))

print("*"*40)
print(add.__doc__)
print(mul.__doc__)
