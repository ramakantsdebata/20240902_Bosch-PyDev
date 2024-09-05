## LEGB - Local-External-Global-Builtin
'''
def Outer():
    # global s1                  # Works: sets the alias s1 to the global object
    # s1 = "Outer String"
    # global s1               # ERROR: Alias already taken

    def Inner():
        # global s1
        # nonlocal s1
        # s1 = "Inner String"
        print(f"Inner --> {s1}")

    s1 = "Outer String"
    Inner()
    print(f"Outer --> {s1}")
    # return Inner


s1 = "Global String"
Outer()
# fn = Outer()
# fn()
# Outer()()
print(f"Global --> {s1}")
'''

def Outer():
    s1 = "Outer String"

    def Inner():
        s1 = "Inner String"
        print(f"Inner --> {s1}")

    Inner()
    print(f"{globals()=}\n\n{locals()=}")
    print(f"Outer --> {s1}")
    print(f"Outer --> {globals()['s1']}")


s1 = "Global String"
Outer()
print(f"Global --> {s1}")
