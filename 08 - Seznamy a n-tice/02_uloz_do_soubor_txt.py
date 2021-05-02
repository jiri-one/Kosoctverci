seznam_slov = []
with open("index.dic", encoding="utf-8") as soubor:
    for cislo_radku, radek in enumerate(soubor):
        if cislo_radku != 0 and radek[0].isupper() is not True:
            seznam_slov.append(radek.split("/")[0].rstrip())

with open("soubor.txt", mode='w', encoding="utf-8") as soubor_txt:
    for slovo in seznam_slov:
        print(slovo, file=soubor_txt)

