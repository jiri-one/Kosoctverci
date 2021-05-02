# napsal jsem to možná zbytečně trochu dlouze, ale vím, že se mi to hodí, protože pak to budu ošetřovat :D
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

# test
seznam_souradnic = [(0, 0)]
pohyb(seznam_souradnic, 'j')
print(seznam_souradnic)         # → [(0, 0), (1, 0)]
pohyb(seznam_souradnic, 'j')
print(seznam_souradnic)         # → [(0, 0), (1, 0), (2, 0)]
pohyb(seznam_souradnic, 'v')
print(seznam_souradnic)         # → [(0, 0), (1, 0), (2, 0), (2, 1)]
pohyb(seznam_souradnic, 'z')
print(seznam_souradnic)         # → [(0, 0), (1, 0), (2, 0), (2, 1), (2, 0)]