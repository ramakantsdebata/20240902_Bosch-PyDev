__all__ = ["greet", "greetName", "greetInteract"]

def greet():
    print("Hi there")

def greetName(name):
    greeting = "Hi"
    final = prep_greeting(greeting, name)
    print(final)

def prep_greeting(greeting, name):
    res = greeting + " " + name + "!!"
    return res

def greetInteract():
    name = input("Enter your name:")
    greeting = "Hi"
    final = prep_greeting(greeting, name)
    print(final)
