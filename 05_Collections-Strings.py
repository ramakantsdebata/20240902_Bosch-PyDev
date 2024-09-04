'''
Immutable
    * Number
    * Srtings
    * Tuples - ()
    * FrozenSet - frozenset()

Mutable
    * Lists - []
    * Sets - {} - Collection of keys
    * Dictionary - {} - Collection of key-value pairs

UDTs - As customised
'''

## Strings
# 'Test' "Test"

s1 = "Returning Abhijeet's book"
s2 = 'He said, "Thank you"'

print(s1)
print(s2)

s3 = '''
This 
is a
multiline
comment
'''
 
print(s3)


# "File".`$datetime``
s4 = "First""Second"

print(s4)

trng = "Python"
days = 5
message = "This is a {} training for {} days".format(trng, days)
message = f"This is a {trng} training for {days} days"
message = "This is a %s training for %d days"%(trng, days)

print(message)

###################################################################################
## Slicing

print(message[0:6])
print(message[:6])
print(message[6:])
print(message[:])
print(message[0:10:2])
print(message)
print("--> [", message[-2:3], "]", sep='')
print("-->", message[:3])
print("-->", message[-2:])
print(message[::-1])
print(message[::2]) # Even
print(message[1::2]) # Odd
print(message[:3:-1])

s1 = "String"
print("[", s1[4:2], "]", sep='')
print("[", s1[4:2:-1], "]", sep='')
print("[", s1[2:4:-1], "]", sep='')
print("[", s1[2::-1], s1[:4:-1], "]", sep='')
print("[", s1[2::-1], s1[-1:4:-1], "]", sep='')

if s1.endswith("ing"):
    print(True)

if s1.startswith("Str"):
    print(True)

print(s1)
print(s1[-1])
print(s1[len(s1) - 1])
