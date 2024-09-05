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

# def Test():
#     greet()
#     greetName("Testing")
#     print(prep_greeting("Hello", "Name"))

print("__name__:", __name__, "  ", type(__name__))

# if __name__ == "__main__":
#     Test()



if __name__ == "__main__":
    greet()
    greetName("Testing")
    print(prep_greeting("Hello", "Name"))


'''
//add.c
// Usage: add 1 2
// Prints 3
int main(int argc, char* argv[])
{
    if (argc != 3)
        print("Incorrect no. of args");
        exit(-1);

    printf("%s", argv[0])
    int a = atoi(argv[1]);
    int b = atoi(argv[2]);
    print("%d", a + b);

    return 0;
}

gcc -o add add.c
'''