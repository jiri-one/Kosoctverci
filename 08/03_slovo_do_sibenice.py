from random import randint

# první varianta
def slovo_do_sibenice_ze_souboru(jmeno_souboru: str):
    with open(jmeno_souboru, encoding="utf-8") as file:
        lines = file.readlines()
        return lines[randint(0, len(lines)-1)]

slovo = slovo_do_sibenice_ze_souboru("soubor.txt")

# testy
print(slovo)