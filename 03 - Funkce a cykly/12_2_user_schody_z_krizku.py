print("Budeme kreslit schody z písmen X.")
pocet_schodu = int(input("Zadej počet schodů: "))
for opakovani in range(1,pocet_schodu+1):
    for _ in range(opakovani):
        print("x", end=" ")
    print()
