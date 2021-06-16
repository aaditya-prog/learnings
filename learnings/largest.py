print("Hello")


initial = -1
list = [9, 19, 234, 23, 54, 1]

# finding smallest
smallest = None
for num in [9, 19, 234, 23, 54, 6]:
    if smallest is None:
        smallest = num
    elif num < smallest:
        smallest = num
print("The smallest number is: ", smallest)

largest = None
for num in [9, 19, 234, 23, 54, 6]:
    if largest is None:
        largest = num
    elif num > largest:
        largest = num
print("The largest number is: ", largest)

# finding largest
for num in list:
    if num > initial:
        initial = num
print("The largest number is: ", initial)

# count number of items in list
count = 1
for num in list:
    count = count + 1
print("List consists of", count, "numbers.")

# sum
total = 0
for num in list:
    total = total + num
print(total)

# average
count = 1
total = 0
for num in list:
    count = count + 1
    total = total + num
    average = total / count
print(average)

# search
for value in list:
    if value > 233:
        print(value, "is larger than 233")

# finding numbers in List
found = False
for val in list:
    if val == 19:
        found = True
        print(found)
