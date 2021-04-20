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
    seznam_souradnic.pop(0)

