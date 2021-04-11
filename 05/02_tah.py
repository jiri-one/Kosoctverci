def tah(hraci_pole, index, symbol):
	"""Vrátí herní pole s daným symbolem umístěným na danou pozici:
	`hraci_pole` je herní pole, na které se hraje.
	`index` je číslo políčka. Čísluje se od nuly, prostě standardní index.
	`symbol` může být 'x' nebo 'o', podle toho jestli je tah za křížky
	nebo za kolečka.
	"""
	return hraci_pole[:index] + symbol + hraci_pole[index+1:]