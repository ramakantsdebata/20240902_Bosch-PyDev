fruits = ['apple', 'banana', 'cherry', 'dragonfruit', 'fig', 'grapes', 'jackfuit', 'kiwi']

# lucky_fruits = []
# for fr in fruits:
#     if 'a' in fr:
#         lucky_fruits.append(fr)
# print(lucky_fruits)

lst = [fr          for fr in fruits       if 'a' in fr];                print(type(lst), lst)
tup = tuple(fr          for fr in fruits       if 'a' in fr);           print(type(tup), tup)
st =  {fr          for fr in fruits       if 'a' in fr};                print(type(st), st)
dt =  {fr: len(fr) for fr in fruits       if 'a' in fr};                print(type(dt), dt)
gen = (fr          for fr in fruits       if 'a' in fr);                print(type(gen), gen)



#################################################

even_numbers = []

for num in range(20):
    if num%2 == 0:
        even_numbers.append(num)

print(even_numbers)