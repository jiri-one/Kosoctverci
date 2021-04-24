def nakresli_mapu(seznam_souradnic: list, jidlo: list):
    for radek in range(10):
        for sloupec in range(10):
            radek_a_sloupec = (radek, sloupec)
            if radek_a_sloupec in jidlo:
                print("? ", end="")
            elif radek_a_sloupec in seznam_souradnic:
                print("X ", end="")
            else:
                print(". ", end="")
        print()

# test
nakresli_mapu([(0, 0), (1, 0), (2, 2), (4, 3), (8, 9)], [(2, 3), (4, 5)])
