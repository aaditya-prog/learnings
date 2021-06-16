# holds key, value pair, mutable
dict1 = {1: "Javascript", 2: "java", 3: "C"}
print(dict1)

a = dict1.keys()
print(a)

b = dict1.values()

c = dict1.items()
print(c)

dict1[4] = "Python"
print(dict1)

del dict1[4]
print(dict1)

dict1.pop(1)
print(dict1)
