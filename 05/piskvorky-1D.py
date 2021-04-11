def vyhodnot(hraci_pole):
	"Vyhodnotí stav hracího pole a vrátí vítěze, remízu nebo řekne, že hra ještě neskončila"
	if len(hraci_pole) == 20 and isinstance(hraci_pole, str):
		if "xxx" in hraci_pole:
			return "x"
		elif "ooo" in hraci_pole:
			return "o"
		elif "-" not in hraci_pole:
			return "!"
		else:
			return "-"
	else:
		print("Špatné hrací pole!")

def tah(hraci_pole, index, symbol):
	"""Vrátí herní pole s daným symbolem umístěným na danou pozici:
	`hraci_pole` je herní pole, na které se hraje.
	`index` je číslo políčka. Čísluje se od nuly, prostě standardní index.
	`symbol` může být 'x' nebo 'o', podle toho jestli je tah za křížky
	nebo za kolečka.
	"""
	try:
		if index not in (range(20)):
			print("Tam nejde hrát!")
			raise ValueError
		elif hraci_pole[index] != "-":
			print("Obsazeno!")
			raise ValueError
		elif symbol != "x" and symbol != "o":
			print(f"Špatný symbol! pouze 'x' nebo 'o'")
			raise ValueError
		else:
			nove_herni_pole = hraci_pole[:index] + symbol + hraci_pole[index+1:]
			print(f"Nový stav hry je: {nove_herni_pole}")
			return nove_herni_pole
	except ValueError:
		pass # zatím pass, uvidíme jak to bude dál

def tah_hrace(pole, symbol):
	"""Zeptá se hráče na tah a vrátí nové herní pole:
	`pole` je herní pole, na které se hraje.
	`symbol` může být 'x' nebo 'o', podle toho jestli hráč hraje za křížky
	nebo za kolečka.
	"""
	while hracuv_index := input("Kam chceš hrát? "):
		try:
			hracuv_index = int(hracuv_index)
			nove_herni_pole = tah(pole, hracuv_index, symbol)
			if nove_herni_pole is not None:
				return nove_herni_pole
		except ValueError:
			print("Zadávej jen čísla!")
		

tah_hrace("----x-----o---------", "x")