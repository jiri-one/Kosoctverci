def pohyb(seznam_souradnic: list, smer: str):
    radek, sloupec = seznam_souradnic[-1]
    if smer == "s": radek = radek - 1
    elif smer == "j": radek = radek + 1
    elif smer == "z": sloupec = sloupec - 1
    elif smer == "v": sloupec = sloupec + 1
    
    if (radek, sloupec) in seznam_souradnic or radek < 0 or radek > 9 or sloupec < 0 or sloupec > 9:
        raise ValueError('Game over')
    else:
        seznam_souradnic.append((radek, sloupec))
        seznam_souradnic.pop(0)


def nakresli_mapu(seznam_souradnic: list):
    for radek in range(10):
        for sloupec in range(10):
            radek_a_sloupec = (radek, sloupec)
            if radek_a_sloupec in seznam_souradnic:
                print("X ", end="")
            else:
                print(". ", end="")
        print()

souradnice = [(0, 0), (0, 1), (0, 2)]
while smer := input("Kterým směrem pojedeme? "):
    if smer == "konec":
        break
    else:
        pohyb(souradnice, smer)
        nakresli_mapu(souradnice)
        
    