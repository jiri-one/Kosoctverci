print("Budeme kreslit čtverec z písmen X.")
pocet_x = int(input("Zadej počet X na straně čtverce: "))
for radek in range(pocet_x):
    for _ in range(pocet_x):
        print("X", end=" ")
    print()
