largest = None
smallest = None
while True:
    num = input("Enter a number: ")
    if num == "done" : 
        break
    try:
        m = int(num)
        if largest is None:
            largest = m
        elif m > largest:
            largest = m
        if smallest is None:
            smallest = m
        elif m < smallest:
            smallest = m
    except:
        print("Invalid input")
    continue

print("Maximum is", largest)
print("Minimum is", smallest)

def myLen(xs):
    n = 0
    for _ in xs:
        n = n + 1
    n