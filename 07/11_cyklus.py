def pohyb(seznam_souradnic: list, smer: str):
    radek, sloupec = seznam_souradnic[-1]
    if smer == "s":
        novy_radek = radek - 1
        seznam_souradnic.append((novy_radek, sloupec))
    elif smer == "j":
        novy_radek = radek + 1
        seznam_souradnic.append((novy_radek, sloupec))
    elif smer == "z":
        novy_sloupec = sloupec - 1
        seznam_souradnic.append((radek, novy_sloupec))
    elif smer == "v":
        novy_sloupec = sloupec + 1
        seznam_souradnic.append((radek, novy_sloupec))

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
        
    