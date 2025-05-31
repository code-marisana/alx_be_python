number = int(input("Enter a number to see its multiplication table: "))
iterations = range(1,11)
for iteration in iterations:
    print(f"{number} * {iteration} = {number * iteration}")