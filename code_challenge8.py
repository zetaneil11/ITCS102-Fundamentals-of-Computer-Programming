num = 4
for i in range(num - 1):
    for x in range(i, num):
        print(" ", end = " ")
    for x in range(i):
        print("*", end = " ")
    for x in range(i + 1):
        print("*", end = " ")
    print()

for i in range(num):
    for x in range(i + 1):
        print(" ", end = " ")
    for x in range(i, num - 1):
        print("*", end = " ")
    for x in range(i, num):
        print("*", end = " ")
    print()
