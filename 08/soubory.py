with open("basnicka.txt", encoding="utf-8") as soubor:
    for radek in soubor:
        radek = radek.rstrip()
        print(radek.upper())
