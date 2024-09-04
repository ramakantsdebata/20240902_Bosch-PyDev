a= 10
print(dir(a))
print([member for member in dir(a) if member.startswith("_") == False])

def Test():
    print("Test")

print(type(Test))
'''
class Test
{
    void operator()(int data)
};

t1 = Test()
t1(10)  <-- Function objects/Functors/Predicates
'''

# Filter only the callable members from the non-dunder members' list
# Hint: callable(), getattr()
