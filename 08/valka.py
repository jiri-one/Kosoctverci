from random import shuffle

def vytvor_balicek():
    """Vrátí nový zamíchaný balíček karet."""
    karty = []
    for barva in 'Sr', 'Pi', 'Ka', 'Kr':
        for hodnota in range(1, 14):
            karta = hodnota, barva
            karty.append(karta)
    shuffle(karty)
    return karty


def popis_kartu(karta):
    """Popíše danou kartu; vrací řetězec jako "7♣", "A♠" nebo "Q♥"."""
    hodnota, barva = karta
    if hodnota == 11:
        popis_hodnoty = 'J'
    elif hodnota == 12:
        popis_hodnoty = 'Q'
    elif hodnota == 13:
        popis_hodnoty = 'K'
    elif hodnota == 1:
        popis_hodnoty = 'A'
    elif hodnota == 10:
        # Aby byly všechny hodnoty jednopísmenné,
        # a líp se to pak vypisovalo,
        # desítku označíme římským číslem.
        popis_hodnoty = 'X'
    else:
        popis_hodnoty = str(hodnota)

    if barva == 'Sr':
        popis_barvy = '♥'
    elif barva == 'Pi':
        popis_barvy = '♠'
    elif barva == 'Ka':
        popis_barvy = '♦'
    else:
        popis_barvy = '♣'

    return popis_hodnoty + popis_barvy

def porovnej_karty(karta_a, karta_b):
    """Porovná hodnoty dvou karet.

    Vrací:
    * 'A', je-li lepší karta_a,
    * 'B', je-li lepší karta_b,
    * None, mají-li stejnou hodnotu.
    """
    if karta_a[0] > karta_b[0]:
        return "A"
    elif karta_a[0] < karta_b[0]:
        return "B"
    else: # tohle by tady v zásadě asi nemuselo být :)
        return None
    
# testy
karty = vytvor_balicek()
print(porovnej_karty(karty[10], karty[20]))