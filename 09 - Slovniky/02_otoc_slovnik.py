slovnik = {'Jablko': 'Apple', 'Knoflík': 'Button', 'Myš': 'Mouse'}

def otoc_slovnik(slovnik):
    otoceny_slovnik = dict()
    for klic, hodnota in slovnik.items():
        otoceny_slovnik[hodnota] = klic
    return otoceny_slovnik

# testy
print(slovnik)
print(otoc_slovnik(slovnik))