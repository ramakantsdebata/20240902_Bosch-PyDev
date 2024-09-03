# Lists [Mutable] - Ordered Collection of non-homogeneous objects

# l1 = []
# l2 = list()
# s1 = "Test STring"
# for x  in s1:
#     l1.append(x)
# print(f"{l1=}, {s1=}")
# print()
# l3 = list("Test String")
# print(l3)
# lst1 = [1, 2, 3, "Bosch"]
# lst2 = [6, 7, "Bangalore", lst1]

# print(len(lst2))
# print(lst2[2])
# print(lst2[3][3])

# from random import randint 

# lst1 = []
# lst2 = []
# lst3 = []
# lst4 = []
# lst5 = []

# dataLst = [lst1, lst2, lst3, lst4, lst5]

# for lst in dataLst:
#     for _ in range(randint(3, 9)):
#         lst.append('a')

# print(dataLst)



'''
lst1 = [1, 2, 3, 4, 5]
if 20 in lst1:
    print(True)


lst2 = [4, 5, 6, 7, 8]

lst3 = lst2 + lst1
print(lst3)


lst4 = ["Test" * 4]     # "Test""Test"...
print(lst4)

lst5 = ["Test"] * 4
print(lst5)

lst6 = [1, 2, 3] + [4, 5, 6]
print(lst6)

len(lst6)  # lst6.__len__()
## sum, min, max

print(max(lst6))

'''


str1 = "Manish"
str2 = str1
print(id(str1), id(str2), sep='\n')
str1 += "!!"

print(f"{str1=}, {str2=}")


lst1 = [1, 2, 3, 4, 5]
print(type(lst1[:]))
lst2 = lst1[:]
print(f"{id(lst1)=}, {id(lst2)=}", sep='\n')
lst1[1] = 200

print(f"{lst1=}, {lst2=}")

lst2 = [4, 1, 7, 3, 8, 3]
lst2.sort()
print(lst2)
print(lst2.count(3))

lst2.reverse()
print(lst2)
# print(lst2.index(2))
print(lst2.pop(2))
print(lst2)