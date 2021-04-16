from util import tah
from random import randint, choice

def strategie_ai(pole, symbol):
    """Vrátí index navržený dle nějakých lepších strategických pravidel."""
    # 1. počítač může svým tahem rovnou vyhrát hru
    if "-" + 2 * symbol in pole: return pole.index("-" + 2 * symbol) # vrátí volný index od např. -xx
    elif 2 * symbol + "-" in pole: return pole.index(2 * symbol + "-") + 2 # vrátí volný index od např. xx-
    elif symbol + "-" + symbol in pole: return pole.index(symbol + "-" + symbol) + 1 # vrátí volný index od např. x-x      
    # 2. může protihráč svým tahem rovnou vyhrát hru (lze zablokovat přidáním znaku zleva, zprava nebo doprostřed)
    hrace = [z for z in ["x", "o"] if z is not symbol][0] # jakože symbol hráče
    if "-" + 2 * hrace in pole: return pole.index("-" + 2 * hrace) # blokuje hráče, pokud má např. -xx
    elif 2 * hrace + "-" in pole: return pole.index(2 * hrace + "-") + 2 # blokuje hráče, pokud má např. xx-
    elif hrace + "-" + hrace in pole: return pole.index(hrace + "-" + hrace) # blokuje hráče, pokud má např. x-x
    # 3. můžu si udělat další další svůj symbol vedle už jednoho svého symbolu
    if symbol in pole:
        indexes = [index for index, char in enumerate(pole) if char == symbol] # udělám seznam indexů, kam už táhl
        while True:
            index = choice(indexes) # vyberu náhodně jeden index, kam by chtěl táhnout
            if len(indexes) > 1: # pokud je tam pořád víc míst, kam by mohl táhnout, ...
                indexes.remove(index) # ... tak rovnou odeberu ten jeden, se kterým to zkouší teď
            try:
                # vyberu tu ideální variantu, kdy má na obě strany volná dvě políčka
                if pole[index-2] == "-" and pole[index+2] == "-" and pole[index-1] == "-" and pole[index+1] == "-":
                    return choice([index-2, index-1, index+2, index+1])
                # případně vyberu variantu, kdy má volno 2x vlevo a 1x vpravo
                elif pole[index-2] == "-" and pole[index-1] == "-" and pole[index+1] == "-":
                    return choice([index-2, index-1, index+1])
                # případně vyberu variantu, kdy má volno 2x vpravo a 1x vlevo
                elif pole[index+2] == "-" and pole[index+1] == "-" and pole[index-1]  == "-":
                    return choice([index+2, index+1, index-1])
            except IndexError:
                pass
    # 4. jinak umístím symbol kamkoliv, jako v původní verzi
    else:
        return randint(0,19)


def tah_pocitace(pole, symbol):
    """Vrátí herní pole se zaznamenaným tahem počítače:
    `pole` je herní pole, na které se hraje.
    `symbol` může být 'x' nebo 'o', podle toho jestli hráč hraje za křížky
    nebo za kolečka.
    """
    print("Teď táhne počítač.")
    if "-" not in pole:
        raise ValueError("Pole je plně obsazené!")
    while True:
        index_pocitace = strategie_ai(pole, symbol) # jedinou změnu jsem udělal na tomto řádku
        try:
            nove_herni_pole = tah(pole, index_pocitace, symbol)
            return nove_herni_pole
        except ValueError as error:
            print(error)
