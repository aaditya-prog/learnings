str = "banana"
letter = str[1]
print(letter)

x = 4
w = str[x - 1]
print(w)

length = len(str)
print("Length", length)

for letter in str:
    print(letter)

count = 0
for letter in str:
    if letter == "a":
        count = count + 1
print(count)


slice = str[2:6]
print(slice)
