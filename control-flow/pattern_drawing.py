square = int(input("Enter the size of the pattern: "))

length = square
width = square

while width > 0:
    for i in range(length):
        print("*", end="")
    print("\n")
    width -= 1
