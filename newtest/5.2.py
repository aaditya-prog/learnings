largest = None
smallest = None
while True:
    val = input("Enter a number: ")
    if val == "done":
        break
    try:
        fval = float(val)
    except:
        print("Invalid input")
        continue

    if largest is None:
        largest = fval
    elif fval > largest:
        largest = fval

    if smallest is None:
        smallest = fval
    elif fval < smallest:
        smallest = fval
print("Maximum is", int(largest))
print("Minimum is", int(smallest))
