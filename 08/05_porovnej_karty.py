def porovnej_karty(karta_a, karta_b):
    """Porovná hodnoty dvou karet.

    Vrací:
    * 'A', je-li lepší karta_a,
    * 'B', je-li lepší karta_b,
    * None, mají-li stejnou hodnotu.
    """
    hodnota_a, barva_a = karta_a
    hodnota_b, barva_b = karta_b
    if hodnota_a > hodnota_b:
        return "A"
    elif hodnota_a < hodnota_b:
        return "B"
    else: # tohle by tady v zásadě asi nemuselo být :)
        return None
    
# testy
karty = vytvor_balicek()
print(porovnej_karty(karty[10], karty[20]))