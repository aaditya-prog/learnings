def multiply(num):
    for i in num:
        yield i * i


my_nums = multiply([1, 2, 3, 4, 5])

for num in my_nums:
    print(num)
