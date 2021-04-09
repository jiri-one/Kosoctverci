for radek in range(1,7):
    for sloupec in range(1,7):
        if radek == 1 or radek == 6 or sloupec == 1 or sloupec == 6:
            print("X", end=" ")
        else:
            print(" ", end=" ")
    print()
