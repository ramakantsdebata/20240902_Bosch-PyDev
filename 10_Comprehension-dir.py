a= "Test"
print(dir(a))
print([member for member in dir(a) if member.startswith("_") == False])