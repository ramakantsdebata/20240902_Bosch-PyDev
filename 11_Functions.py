## Define Earlier (Python) vs. Define Higher
'''
def Bar():
    print("Bar")
    Baz()

def Foo():
    print("Foo")
    Bar()

def Main():
    print("Main")
    Foo()

def Baz():
    print("Baz")

Main()
'''
############################
'''
# C/CP code illustration
void Baz(); //Declaration

void Bar()
{
    Baz()
}

void Baz()
{
    printf("Baz");
}

int main()
{
    Bar()
}


###############################

#include <stdio.h>

int main()
{
    printf("Hi there");
    return 0;
}


##################################

class A;    // Forward declaration

class B
{
    A* ptr;
    ....
};

class A
{
    B obj;
};

'''

###############################################################################
'''
def add(a, b):
    print(f"{a=}, {b=}")
    sum = a + b
    return sum

print(add(1, 2))        # Positional args
print(add(b=1, a=2))    # Named args
'''
'''
def add(a, b=0, c=0):
    print(f"{a=}, {b=}, {c=}")
    sum = a + b + c
    return sum

print(add(1, 2, 3))
print(add(1, 2))
print(add(1, b=2, c=3))
print(add(1, c=3))

def FileOpen(fileName, mode="r", encoding="utf-8", bSharing=False):
    pass

# FileOpen()
# FileOpen(mode="w")
FileOpen("test.txt")
FileOpen("test.txt", mode="w")
FileOpen("test.txt", encoding="utf-16")
FileOpen("test.txt", mode="w", encoding="utf-32", bSharing=True)
FileOpen("test.txt", "w", "utf-32", True)
# FileOpen("test.txt", mode="w", encoding="utf-32", True)   # SyntaxError: positional argument follows keyword argument
'''

###############################################################################
## Sequence Unpacking & Packing
a = 1
b = 2
a, b = 1, 2

lst1 = [1, 2]
a, b = lst1     # Unpacking

lst2 = [1, 2, 3, 4, 5, 6, 7]
a, b, c, *others = lst2         # '*' is being used as a Packing operator, as it is on the LHS (recipient)

print(f"{a=}, {b=}, {c=}, {others=}, {type(others)=}")


def add(a, b, c=0, d=0):
    return a + b

print(f"{add(lst1[0], lst1[1])=}")
print(f"{add(*lst1)=}")         # '*' is being used as an Unpacking operator, as it is used in the call (NOT the dfinition) i.e. sender

# def mul(a, b, c=1, d=1):
def mul(a, b, *more_data):
    print(f"{a=}, {b=}, {more_data=}, {type(more_data)=}")
    prod = a * b
    for val in more_data:
        prod *= val
    return prod

print("\n", "*"*40)
print(f"{mul(1, 2)=}")
print(f"{mul(1, 2, 3, 4)=}")
print(f"{mul(1, 2, 3, 4, 5, 6, 7)=}")

