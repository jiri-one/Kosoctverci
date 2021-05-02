print("Budeme kreslit prázdný čtverec z písmen X.")
pocet_x = int(input("Zadej počet X na straně čtverce: "))
for radek in range(pocet_x):
    for sloupec in range(pocet_x):
        if radek == 0 or radek == pocet_x-1 or sloupec == 0 or sloupec == pocet_x-1:
            print("X", end=" ")
        else:
            print(" ", end=" ")
    print()
