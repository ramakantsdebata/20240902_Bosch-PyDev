## Dictionary - [Mutable] Collection of 'key-value' pair. 
#       Key - hash-able (Immutable)
#       Value - Any type

'''
dt = dict()
print(type(dt), dt)


dt1 = {"John": 96, "Jane": 92, "Joe": 87}
print(dt1)

st1 = set(dt1)
print(f"{st1=}")

fs1 = frozenset([1, 2, 3])
st2 = {'a', 'b', 'c', fs1}

dt2 = dict.fromkeys(st2)
print(dt2)

print(len(dt2))

for key in dt2.keys():
    print(key, end=" ")
print()

for value in dt1.values():
    print(value, end=" ")
print()

for key, value in dt1.items():
    print(key, value, end=" --- ")
print()

print(dt1['Joe'])

if 'Jack' in dt1:
    print(dt1['Jack'])
else:
    print("No such data!")

print("-->", dt1.get('Jack'))

print(dt1.pop('Joe'))
# print(dt1.pop('Joe'))

print(dt1.popitem())

l1 = list(dt2)
print(type(l1), l1)

print(dt1)
# Add a k-vpair to dt1 - ('a': 100)
dt1['a'] = 100
print(dt1)

dt1.update(dt2)
print(dt1)      # What haappens to the value of 'a', old value or new value ?


# # dt1[dt2] = 500
# # print(dt1)
'''
###############################################################################
## Named Tuple

point1 = (10, 20)
print(f"x = {point1[0]}, y = {point1[1]}")

from collections import namedtuple

Point = namedtuple('Point_data', 'x y')
p1 = Point(10, 20)
p2 = Point(40, 50)

print(f"x = {p1[0]}, y = {p1[1]}")
print(f"x = {p1.x}, y = {p1.y}")
print(f"{p1.x=}, {p1.y=}")


# Student = namedtuple('Student_data', 'roll name std')
Student = namedtuple('Student_data', ['roll', 'name', 'std'])
s1 = Student(17, "Rakesh", 6)
print(s1)
print(f"{s1.roll=}, {s1.name=}, {s1.std=}")

print(type(Student), Student)

print(hash(s1))

'''
Common between Set and dictionary
        {}
        key - hashable, immutable

Nest a set in a set --> Not possible; Use FrozenSets, which is immutable and can be used as a key.

Nest a dictionary in a dictionary (as a key) --> Not possible; Use a NamedTuple, which is Immutable.
'''


lst = [1, 2, 3]
lst1 = [1, 2, 3, lst]
dt1 = dict.fromkeys(lst1)
print(dt1)