## Dictionary - Collection of 'key-value' pair. 
#       Key - hash-able (Immutable)
#       Value - Any type


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
dt1.update(dt2)
print(dt1)