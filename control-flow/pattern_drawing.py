rows = int(input("Enter the size of the pattern:"))
columns = rows
while columns > 0:
    for i in range(rows):
        print("*",end="")
    print("\n")
    columns-=1