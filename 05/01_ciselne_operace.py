# nějak mi přišlo, že tohle řešní bude lepší ve třídě, doufám, že to nevadí

class ZakladniKalkulacka():
	def __init__(self):
		self.operatori = {'+': lambda x, y: x + y,
						  '-': lambda x, y: x - y,
						  '*': lambda x, y: x * y,
						  '/': lambda x, y: x / y}
		self.spusteni_operace()
		
	def nacteni_cisel(self):
		while True:
			try:
				input1 = int(input("Zadej první číslo: "))
				input2 = int(input("Zadej druhé číslo: "))
				return input1, input2
			except ValueError:
				print("Zadej číslo číslem brácho :-)")
			

	def nacteni_operace(self):
		while True:
			operace = input("Zadej operaci: ")
			if operace not in self.operatori.keys():
				print('Musíš zadat "+", "-", "*", "/", nic jiného program nezná.')
			else:
				return operace

	def spusteni_operace(self):
		cislo1, cislo2 = self.nacteni_cisel()
		operace = self.nacteni_operace()
		try:
			print(f"Výsledek je: {self.operatori[operace](cislo1, cislo2)}")
		except ZeroDivisionError:
			print("Nulou dělit nelze! Takže výsledek nedostaneš!")

		
if __name__ == "__main__":
	zakladnikalkulacka = ZakladniKalkulacka()