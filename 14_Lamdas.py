def square(num):
    return num**2

print(type(lambda val: val**2))

sq = lambda val: val**2
print(sq(9))

IsEven = lambda num : True if num%2 == 0 else False
print(IsEven(22))
print(IsEven(23))


tools = {
    "square":lambda val: val**2, 
    "IsEven": lambda num : True if num%2 == 0 else False
    }


print(tools["square"](9))