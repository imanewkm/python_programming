largest = None
smallest = None

while True:
    num = input("Enter a number: ")
    if num == "done":
        break
    try:
        num_int = int(num)
        if largest is None or num_int > largest:
            largest = num_int
        if smallest is None or num_int < smallest:
            smallest = num_int
    except ValueError:
        print("Invalid input")

if largest is not None:
    print(f"Maximum is {largest}")
    print(f"Minimum is {smallest}")
else:
    print("Invalid input")