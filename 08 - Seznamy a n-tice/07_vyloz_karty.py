balicek_a, balicek_b, stul = rozdej_balicky()

def vyloz_karty(balicky):
    """Vyloží karty obou hráčů na stůl.

    "balicky" je trojice: balíček hráče A, balíček hráče B, karty na stole.

    Každý z hráčů vyloží poslední kartu svého balíčku na stůl.
    Nemá-li hráč co vyložit, nastane výjimka `SystemExit`.
    (To zjednodušuje zbytek hry.)

    Funkce vypisuje co dělá pomocí "print".
    (To taky zjednodušuje zbytek hry.)
    """
    balicek_a, balicek_b, na_stole = balicky
    try:
        karta_a = balicek_a.pop()
    except IndexError:
        raise SystemExit('Hráč B vyhrál')
    try:
        karta_b = balicek_b.pop()
    except IndexError:
        raise SystemExit('Hráč A vyhrál')
    print(f"Hráč A hraje kartu {popis_kartu(karta_a)}")
    print(f"Hráč B hraje kartu {popis_kartu(karta_b)}")
    na_stole.append(karta_a)
    na_stole.append(karta_b)

# test
vyloz_karty((balicek_a, balicek_b, stul))