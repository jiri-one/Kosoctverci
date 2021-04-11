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
			return hraci_pole[:index] + symbol + hraci_pole[index+1:]
	except ValueError:
		pass # zatím pass, uvidíme jak to bude dál

print(tah("----x-----o---------", 5, "bl"))
	