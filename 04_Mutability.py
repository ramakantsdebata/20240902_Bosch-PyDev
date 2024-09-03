count = 0
a = b = 0
for x in range(1000):
    if a is b:
        print(".", end='')
    else:
        print(f"\nDistinct objects at value {a}")
        count += 1
        if count >= 10:
            break
    a += 1
    b += 1
else:
    print("Completed!")

p = 10
q = 11
q -= 1

print(p, q, id(p), id(q))
if p is q:
    print(True)
else:
    print(False)


def obj_chars(obj):
    print(obj, type(obj), id(obj))


p = 10
obj_chars(p)

q = "Some String"
obj_chars(q)


'''
== -> value of 'a' is equal to value of 'b'
is -> id(a) is equl to id(b)
'''


print("="*40)

a = 10
print(a, id(a))
a += 1
print(a, id(a))


name = "Python"
print(id(name), name)
name += " Training"
print(id(name), name)


name[0] = 'p'
print(id(name), name)