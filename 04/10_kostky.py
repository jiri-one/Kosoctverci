from random import randint

def hod_kostkou():
	return randint(1, 6)

best_score, best_hrac = 0, 0

for hrac in range(1,5):
	print(f"Hraje hráč č.{hrac}.")
	pocet_hodu_na_6 = 0
	while hozene_cislo := hod_kostkou():
		#_ = input("Napiš cokoliv a hodíš kostkou: ") # varianta ručně
		print(f"Hráči č.{hrac} házíš kostkou a hodil jsi: {hozene_cislo}")
		pocet_hodu_na_6 += 1
		if hozene_cislo == 6:
			print(f"Hráči č.{hrac}, konečně jsi hodil šestku, měl jsi na to {pocet_hodu_na_6} pokusů.")
			if pocet_hodu_na_6 > best_score:
				best_score = pocet_hodu_na_6
				best_hrac = hrac
			break
		else:
			print("Protože nepadlo 6, tak házíš znovu!")

print(f"Vyhrál hráč č.{best_hrac} a potřeboval na to {best_score} pokusů. Gratulace!")
	