from random import randint

def pohyb(seznam_souradnic: list, smer: str):
    radek, sloupec = seznam_souradnic[-1]
    if smer == "s": radek = radek - 1
    elif smer == "j": radek = radek + 1
    elif smer == "z": sloupec = sloupec - 1
    elif smer == "v": sloupec = sloupec + 1
    
    if (radek, sloupec) in seznam_souradnic or radek < 0 or radek > hriste[0]-1 or sloupec < 0 or sloupec > hriste[1]-1:
        raise ValueError('Game over')
    else:
        if (radek, sloupec) in jidlo:
            jidlo.remove((radek, sloupec))
            jidlo.append((randint(0, hriste[0]-1), randint(0, hriste[1]-1)))
        else:
            seznam_souradnic.pop(0)
        seznam_souradnic.append((radek, sloupec))
        
def nakresli_mapu(seznam_souradnic: list, jidlo: list):
    for radek in range(hriste[0]):
        for sloupec in range(hriste[1]):
            radek_a_sloupec = (radek, sloupec)
            if radek_a_sloupec in jidlo:
                print("? ", end="")
            elif radek_a_sloupec in seznam_souradnic:
                print("X ", end="")
            else:
                print(". ", end="")
        print()


souradnice = [(0, 0), (0, 1), (0, 2)]
jidlo = [(2, 3), (4, 5)]
hriste = (30, 20)
while smer := input("Kterým směrem pojedeme? "):
    if smer == "konec":
        break
    else:
        pohyb(souradnice, smer)
        nakresli_mapu(souradnice, jidlo)
        
    