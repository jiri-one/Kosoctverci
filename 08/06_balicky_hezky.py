def balicky_hezky():
    print("Hráč A\t Hráč B")
    balicek_a, balicek_b, stul = rozdej_balicky()
    for karta_a, karta_b in zip(balicek_a, balicek_b):
        karta_popsana_a, karta_popsana_b = popis_kartu(karta_a), popis_kartu(karta_b), 
        print(f"{karta_popsana_a}\t\t {karta_popsana_b}")

balicky_hezky()