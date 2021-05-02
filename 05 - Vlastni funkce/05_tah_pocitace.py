from random import randint
def tah_pocitace(hraci_pole, symbol):
    """Vrátí herní pole se zaznamenaným tahem počítače:
    `pole` je herní pole, na které se hraje.
    `symbol` může být 'x' nebo 'o', podle toho jestli hráč hraje za křížky
    nebo za kolečka.
    """
    while index_pocitace := randint(0,19):
        if hraci_pole[index_pocitace] == "-":
            nove_herni_pole = hraci_pole[:index_pocitace] + symbol + hraci_pole[index_pocitace+1:]
            print(f"Nový stav hry je: {nove_herni_pole}")
            return nove_herni_pole

tah_pocitace("----x-----o---------", "x")