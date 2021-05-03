# neřešil jsem velikost písmen, protože to není v zadání

def pocet_znaku(retezec: str):
    # kdyby bylo potreba resit velikost pismen
    # retezec.lower()
    pocetni_slovnik = {}
    for pismeno in retezec:
        if pismeno in pocetni_slovnik:
            pocetni_slovnik[pismeno] += 1
        else:
            pocetni_slovnik[pismeno] = 1
    return pocetni_slovnik

# testy
print(pocet_znaku("hello world"))
print(pocet_znaku("booomta rata"))
print(pocet_znaku("Booomta rata boom"))