import re

string = "The Euro STOXX 600 index, which tracks all stock markets across Europe \
including the FTSE, fell by 11.48% - the worst day since it launched in 1998. \
The panic selling prompted by the coronavirus has wiped £2.7tn off the value \
of STOXX 600 shares since its all-time peak on 19 February."

# path = r"\c\User\newfile"
# print(path)

s = r"\d{3}"
print(type(s), s)


t = re.compile(s)
print(type(t), t)

# Findall - Returns a list of matches
# res = re.findall(t, string)
res = re.findall(s, string)
res = t.findall(string)
print(type(res), res)



## Search - Stops after the first match 
res = re.search(s, string)
print(type(res), res)
print(res.span()[0], res.span()[1])
print(string[res.span()[0]:res.span()[1]])
print(string[res.start():res.end()])


## Match
res = re.match(r"\w{3}", string)
print(type(res), res)

res = re.match(r"\w{4}", string)
print(type(res), res)


## Fullmatch 
print(len(string))
res = re.fullmatch(r".{285}", string)
print(type(res), res)


## Split
res = string.split(' ')
print(len(res), res)

res = re.split(r'\s', string)
print(len(res), res)


## Sub - Substitute
res = re.sub(r"[isby]{2,}", "*****", string)
print(res)

res = re.sub(r"[^isby]{2,}", "*****", string)
print(res)

res = re.sub(r"[A-Z]{2,}", "*****", string, 2)
print(res)

res = re.sub(r"[A-Z]{2,}", "*****", string)
print(res)

res = re.subn(r"[A-Z]{2,}", "*****", string)
print(res)
