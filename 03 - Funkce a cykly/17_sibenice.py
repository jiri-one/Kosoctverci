from random import randint
slova = ["trávník", "stromek", "stavení"]
slovo = slova[randint(0,2)]

aktual = "_" * len(slovo)
pocet_neuspesnych = 0

print("Zahrajeme si šibenici, budeš hádat písmena (pouze malá), ze slova.")
print("Máš maximálně 9 pokusů!\n\n")

while "_" in aktual:
    print("Počet tvých neúspěšných pokusů je: ", pocet_neuspesnych)
    print("Tohle je aktuální stav hádaného slova:")
    print(aktual)
    hadane_pismeno = input("Napiš písmeno, které si myslíš, že je v hádaném slově: ")
    try:
        index = slovo.index(hadane_pismeno)
        aktual = aktual[:index] + hadane_pismeno + aktual[index+1:]
        print("Uhádl jsi!")
        if "_" not in aktual:
            print(f"""Vyhrál jsi!\nPočet tvých špatných pokusů byl {pocet_neuspesnych}""")    
    except:
        print("Neuhádl jsi!")
        pocet_neuspesnych += 1
        if pocet_neuspesnych == 9:
            print("Počet tvých neúspěchů dosáhl na 9!")
            print(f"Prohrál jsi! Slovo, které jsi neuhádl bylo \"{slovo}\"")
            break
