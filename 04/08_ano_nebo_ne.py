def ano_nebo_ne(otazka):
	"""Vrátí True nebo False podle odpovědi uživatele"""
	while True:
		odpoved = input(otazka)
		odpoved = odpoved.split()
		if odpoved[0] == 'ano' or odpoved[0] == 'a':
			return True
		elif odpoved[0] == 'ne' or odpoved[0] == 'n':
			return False

		print('Nerozumím! Odpověz "ano (a)" nebo "ne (n)".')

# Příklad použití
if ano_nebo_ne('Chceš si zahrát hru? '):
	print('OK! Ale napřed si ji musíš naprogramovat.')
else:
	print('Škoda.')