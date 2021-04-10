# já si myslím, že jsem zapracoval všechno, co bylo požadováno
from random import choice
from obrazek import obrazek
slova = ["trávník", "stromek", "stavení", "čokoláda"]
slovo = choice(slova)

aktual = "_" * len(slovo)
pocet_neuspesnych = 0

def zamen(aktual, hadane_pismeno, index):
	global slovo
	slovo = slovo[:index] + "?" + slovo[index+1:]
	return aktual[:index] + hadane_pismeno + aktual[index+1:]

print("Zahrajeme si šibenici, budeš hádat písmena (pouze malá), ze slova.")
print("Máš maximálně 9 pokusů!\n\n")

while "_" in aktual:
	print("Počet tvých neúspěšných pokusů je: ", pocet_neuspesnych)
	print(obrazek(pocet_neuspesnych))
	print("Tohle je aktuální stav hádaného slova:")
	print(aktual)
	hadane_pismeno = input("Napiš písmeno, které si myslíš, že je v hádaném slově: ")
	if hadane_pismeno == "konec":
		print("Když tě šibenice nebaví, tak končíme!")
		break
	elif len(hadane_pismeno) == 0 or len(hadane_pismeno) > 1:
		print("Jsi osel, jen dvakrát tak ošklivej! Napiš pouze jedno písmeno, které hádáš!")
	elif hadane_pismeno in " \n!\"#$%&\'()*+,-./:;<=>?@[\]^_{|}~":
		print("Jsi osel, jen dvakrát tak ošklivej! Napiš pouze jedno PÍSMENO, které hádáš!")
	else:
		try:
			aktual = zamen(aktual, hadane_pismeno, slovo.index(hadane_pismeno))
			print("Uhádl jsi!")
			if "_" not in aktual:
				print(f"""Vyhrál jsi!\nPočet tvých špatných pokusů byl {pocet_neuspesnych}""")    
		except:
			print("Neuhádl jsi!")
			pocet_neuspesnych += 1
			if pocet_neuspesnych == 9:
				print("Počet tvých neúspěchů je dosáhl na 9!")
				print(obrazek(pocet_neuspesnych))
				print(f"Prohrál jsi! Slovo, které jsi neuhádl bylo \"{slovo}\"")
				break