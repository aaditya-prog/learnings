# lists mutable, heterogenous
list1 = [1, 2, 3, "aaditya"]
print(list1)

# append(), extend(), insert()
list1.append((4, 5))
print(list1)

list1.extend((4, 5))
print(list1)

list1.insert(3, "fourth")
print(list1)

# del, pop(), remove()
del list1[3]
print(list1)

deleted = list1.pop(4)
print(deleted)

list1.remove(2)
print(list1)

# sorting lists
list2 = [1, 500, 3, 5, 7, 4]
print(sorted(list2))
print(list2)

list2.sort()
print(list2)

# find out index
print(list2.index(3))

# count
