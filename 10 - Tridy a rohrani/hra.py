
import sachy

print("""
Šachy pro příkazovou řádku najsou příliš hratelné.
Zkus radši grafickou variantu (ui.py).
""")

input('Stiskni Enter (nebo Ctrl+C pro ukončení)')


sachovnice = sachy.Sachovnice()

tahy = {
    'a': 0,
    'b': 1,
    'c': 2,
    'd': 3,
    'e': 4,
    'f': 5,
    'g': 6,
    'h': 7,
}

def nacti_tah():
    while True:
        odpoved = input('Odkud a kam táhnout (např. b1a3)? ')
        if len(odpoved) != 4:
            print('Zadej 4 písmena/čísla, např. b1a3')
        else:
            tah = []
            try:
                for znak in odpoved.lower():
                    znak = tahy.get(znak, znak)
                    tah.append(int(znak))
            except ValueError:
                print('Zadej 4 písmena/čísla, a-h a 1-9')
            else:
                sloupec_z, radek_z, sloupec_na, radek_na = tah
                return (8-radek_z, sloupec_z), (8-radek_na, sloupec_na)

while True:
    print(sachovnice)
    z, na = nacti_tah()
    sachovnice.vyber_pozici(z)
    sachovnice.tahni_na_pozici(na)
