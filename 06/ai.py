from util import tah
from random import randint

def tah_pocitace(pole, symbol):
    """Vrátí herní pole se zaznamenaným tahem počítače:
    `pole` je herní pole, na které se hraje.
    `symbol` může být 'x' nebo 'o', podle toho jestli hráč hraje za křížky
    nebo za kolečka.
    """
    print("Teď táhne počítač.")
    while index_pocitace := randint(0,19):
        try:
            nove_herni_pole = tah(pole, int(index_pocitace), symbol)
            return nove_herni_pole
        except ValueError:
            pass
