def vytvor_seznam_zvirat():
    return ['pes', 'kočka', 'králík', 'had', 'krocan', 'prase']

def filtruj_kratka_jmena(jmenny_seznam):
    return [kratas for kratas in jmenny_seznam if len(kratas) < 5]

def filtruj_k(jmenny_seznam):
    try:
        return [zvire for zvire in jmenny_seznam if zvire[0] == "k"]
    except IndexError:
        return jmenny_seznam

def obsahuje(jmenny_seznam, zvire):
    return zvire in jmenny_seznam

def bez_prvniho(jmenny_seznam):
    return [zvire for zvire in jmenny_seznam[1:]]
    
# tohle mi přijde jednodušší, samozřejmě pokud to bude požadováno, tak mohu udělat i tu zdlouhavou neefektivní verzi
def serad_od_druheho(seznam):
    jinak_razeny_seznam = seznam.copy()
    jinak_razeny_seznam.sort(key=lambda x: x[1:])
    return jinak_razeny_seznam
    
# testy
zvirata = vytvor_seznam_zvirat()
print(zvirata)
print(serad_od_druheho(zvirata))
print(zvirata)
print(serad_od_druheho([""]))
print(serad_od_druheho([]))

#zvirata = vytvor_seznam_zvirat()
#zvirata_s_kratkym_jmenem = filtruj_kratka_jmena(zvirata)
#zvirata_zacinajici_na_k = filtruj_k(zvirata)
#print(filtruj_k([]))
#print(bez_prvniho([]))


#print(f"Všechna zvířata, i ta s dlouhým jménem, jsou: {zvirata}")
#print(f"Zvířata s krátkým jménem jsou: {zvirata_s_kratkym_jmenem}")
#print(f"Zvířata začínající na 'k' jsou: {zvirata_zacinajici_na_k}")
#print(f"Obsahuje seznam {zvirata} pejska? Odpoved je (anglicky): {obsahuje(zvirata, 'pes')}")
#print(bez_prvniho(zvirata))
#print(bez_prvniho(['pes']))
#print(bez_prvniho([]))