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


# If the string has newlines in it, above will fail
string2 = """The Euro STOXX 600 index, which tracks all stock markets across Europe 
including the FTSE, fell by 11.48% - the worst day since it launched in 1998. 
The panic selling prompted by the coronavirus has wiped £2.7tn off the value 
of STOXX 600 shares since its all-time peak on 19 February."""

print(len(string2))
res = re.fullmatch(r".{288}", string2)  # Fails as the '.' cannot account for the newlines
print(type(res), res)

res = re.fullmatch(r".{288}", string2, re.S|re.I) # re.S = re.DOTALL
print(type(res), res)

# Flags - re.I (ignorecase), re.M (multiline), re.X (verbose)
print("*"*40)
res = re.search(r".+\s(.+ex).+(\d\d\s.+).", string)
res = re.search(r'''.+\s     #Beginning of the string
                (.+ex)       #Searching for index
                .+           #Middle of the string
                (\d\d\s.+).  #Date at the end''', string, re.X)
print(res.groups())


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


# groups

# Metacharacters
# * (zero or more times) 
# + (one or more times)
# ? (zero or one time)
# Greedy vs. Non-greedy  (*?    +?    ??)

# \ 1. Special sequences (\w \W \d \D \A (beg of string) \Z (end of string) ^ (beg of line) $ (end of line) \b \B \s \S)
#   2. Escape \. \[ \] \( \)
# 
# Inside the [] for char set, the special meanings are removed implicitly.

# Extension notations (non capturing groups, Named groups, +ve lookahead, -ve lookahead, +ve lookbehind, -ve lookbehind)
