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


a = 1
b = 2
a, b = 1, 2

lst1 = [1, 2]
a, b = lst1     # Unpacking