# def add(a: int, b: int) -> int:
#     return a + b

# print(add(1, 2))
# print(add("Test", "String"))

###############################################################################

'''
class Animal:
    def talk(self):
        print("Talking...")

class Dog(Animal):
    def talk(self):
        print("woof")

class Cat(Animal):
    def talk(self):
        print("meow")

class Cow(Animal):
    def talk(self):
        print("moo")


def Communicate(obj: Animal):
    obj.talk()


d = Dog()
c = Cat()
cw = Cow()

Communicate(d)
Communicate(c)
Communicate(cw)
Communicate(c)
'''

###############################################################################


class Animal:
    def talk(self):
        print("Talking...")

class Dog:
    def talk(self):
        print("woof")

class Cat:
    def talk(self):
        print("meow")

class Cow:
    def talk(self):
        print("moo")


def Communicate(obj: Animal):
    obj.talk()


d = Dog()
c = Cat()
cw = Cow()

Communicate(d)
Communicate(c)
Communicate(cw)
Communicate(c)

def add(a, b):
    print("Entered the method")
    return a + b

add(d, c)