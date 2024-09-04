# Set - [Mutable] Collection of keys (Only Immutables can be keys as they are hash-able; Have to be unique)

st1 = {1, 2, 3}
print(st1)

def myHash(num):
    return num%10

hash1 = myHash(1427)
hash2 = myHash(2177)
hash3 = myHash(2244)

print(hash1, hash2, hash3)

a = "Name"
hs1 = hash(a)
print(type(hs1), hs1)

b = (1, 2, 3)           # Container - Immutable; Content - Immutable
hs2 = hash(b)
print(hs2)

lst = [1, 2, 3]
c = [1, 2, 3]      # Container - Mutable; Contents - Immutable
# hs3 = hash(c)
# print(hs3)


def IsMutable(obj):
    try:
        hash(obj)
        return False
    except TypeError:
        return True
    
print(IsMutable(a))
print(IsMutable(b))
print(IsMutable(c))

############################################################
## Key is hashable, meaning immutable
## Sets are unordered

st2 = {"One", "Two", "One"}
st2.add("Three")
st2.add("One")
print(st2)
st3 = set(c)
st3.update(st2)
print(st3)



lst1 = [1, 2, 3]
lst2 = [1, 2, 3]
lst3 = lst1
# print(id(lst1[0]), id(lst2[0]), sep="\n")
print(id(lst1), id(lst3), sep="\n")
st1 = set()
st1.update(lst1)
lst1.append(4)
st1.update(lst3)

print(st1)
st1.remove(3)
print(st1)
st1.discard(3)
data = st1.pop()
print(data)    # Retrieves and removes a random key from the set
print(st1)
st1.clear()
print(st1)


## Set Operations #############################################################

st1 = {1, 2, 3, 4}
st2 = {3, 4, 5, 6, 7}
res = st1.union(st2)
print(type(res), res)

print(st1 | st2)
print(st1.intersection(st2), st1 & st2)
print(st1.difference(st2), st1-st2)
print(st1.symmetric_difference(st2), st1^st2)

st3 = {3, 4}
print(st3.issubset(st1), st3 <= st1)
print(st2.issuperset(st3), st2 >= st3)
print(st1.isdisjoint(st2), st1 & st2 == set())


lst1 = [1, 2, 3]
lst2 = [1, 2, lst1]

# st5 = {st1}    # ERROR

tp1 = (1, 2)
tp2 = (1, 2, tp1)   # Success
print(tp2)

###############################################################################
## Frozen Sets

st1 = {1, 2, 3}
fs1 = frozenset([1, 2, 3])

print(st1, fs1, sep="\n")

print(IsMutable(fs1))

st2 = {'a', 'b', 'c', fs1}
print(st2)