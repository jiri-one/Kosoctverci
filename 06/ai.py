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
    if "-" + 2 * hrace in pole: return pole.index("-" + 2 * hrace)
    elif 2 * hrace + "_" in pole: return pole.index(2 * hrace + "-") + 2
    elif hrace + "-" + hrace in pole: return pole.index(hrace + "-" + hrace)  
    # 3. můžu si udělat další další svůj symbol vedle už jednoho svého symbolu
    indexes = [index for index, char in enumerate(pole) if char == symbol]
    if symbol in pole:
        return
    # 4. jinak křížek náhodně kamkoliv, jako v původní verzi
    

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
        index_pocitace = strategie_ai(pole, symbol)
        try:
            nove_herni_pole = tah(pole, index_pocitace, symbol)
            return nove_herni_pole
        except ValueError as error:
            print(error)
