def pohyb(seznam_souradnic: list, smer: str):
    radek, sloupec = seznam_souradnic[-1]
    if smer == "s": radek = radek - 1
    elif smer == "j": radek = radek + 1
    elif smer == "z": sloupec = sloupec - 1
    elif smer == "v": sloupec = sloupec + 1
    seznam_souradnic.append((radek, sloupec))
    seznam_souradnic.pop(0)
