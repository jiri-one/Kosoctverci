seznam_slov = []
with open("index.dic", encoding="utf-8") as soubor:
    for cislo_radku, radek in enumerate(soubor):
        if cislo_radku != 0 and radek[0].isupper() is not True:
            seznam_slov.append(radek.split("/")[0].rstrip())

# tests
print(seznam_slov)
