for i in range (5):
    for x in range (5):
        if x + i == 4 or x == i:
            print("*", end = " ")
        else:
            print(" ", end = " ")
    print()
