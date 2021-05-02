def balicek_hezky():
    karty = vytvor_balicek()
    for karta in karty:
        karta_popsana = popis_kartu(karta)
        print(karta_popsana)


balicek_hezky()