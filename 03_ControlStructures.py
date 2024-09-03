'''
# if-elif-else
name = input("Enter your name: ")
if 'M' in name: 
    print("Hi,", name)
elif 'n' in name:
    print("Capitalise the name,", name)
else:
    print("Who's this?")
'''


# Loops
'''
## For
lst = [1,2,3,4,5]
# for x in lst:
#     print(x**2, end='--')

# Find a number
val = 7
for x in lst:
    if x == val:
        print("Value found")
        break
else:
    print("Value NOT found!")



print("="*40)


ln = len(lst)

for idx in range(1, ln, 2):
    print(lst[idx], end=' ')


iter_count = 5

greet = "Hi"

for _ in range(iter_count):
    print(greet)
'''

'''
## While
it = 5
# it = None
while it > 0:
    print(it)
    it -= 1
    if it == 3 :
        break
else:
    print("All iterations completed")

'''
'''
# Match case
num = 3

match num:
    case 1:
        print("One")
    case 2:
        print("Two")
    case 3:
        print("Three")
    case 4:
        print("Four")
    case 5:
        print("Five")
    case _:
        print("Out of range")
''' 

a = 10
b = 20
c = 30

print(a,b,c, sep='', end="\n***********\n")
print("="*40)
print(a,b,c, sep='-->', end="\n***********\n")

print("")


