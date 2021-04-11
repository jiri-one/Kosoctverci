def tah(hraci_pole, index, symbol):
	"""Vrátí herní pole s daným symbolem umístěným na danou pozici:
	`hraci_pole` je herní pole, na které se hraje.
	`index` je číslo políčka. Čísluje se od nuly, prostě standardní index.
	`symbol` může být 'x' nebo 'o', podle toho jestli je tah za křížky
	nebo za kolečka.
	"""
	try:
		if index not in (range(20)):
			raise ValueError
		elif hraci_pole[index] != "-":
			raise ValueError
		elif symbol != "x" or symbol != "o":
			raise ValueError
		else:
			return hraci_pole[:index] + symbol + hraci_pole[index+1:]
	except ValueError:
		pass # zatím pass, uvidíme jak to bude dál

def tah_hrace(pole, symbol):
	"""Zeptá se hráče na tah a vrátí nové herní pole

	`pole` je herní pole, na které se hraje.
	`symbol` může být 'x' nebo 'o', podle toho jestli hráč hraje za křížky
	nebo za kolečka.
	"""
	while hracuv_index := input("Kam chceš hrát?"):
		tah(pole, hracuv_index, symbol)