from util import tah
from re import match
from ai import tah_pocitace

def vyhodnot(hraci_pole):
    "Vyhodnotí stav hracího pole a vrátí vítěze, remízu nebo řekne, že hra ještě neskončila" 
    if "xxx" in hraci_pole:
        return "x"
    elif "ooo" in hraci_pole:
        return "o"
    elif "-" not in hraci_pole:
        return "!"
    else:
        return "-"

def tah_hrace(pole, symbol):
    """Zeptá se hráče na tah a vrátí nové herní pole:
    `pole` je herní pole, na které se hraje.
    `symbol` může být 'x' nebo 'o', podle toho jestli hráč hraje za křížky
    nebo za kolečka.
    """
    while hracuv_index := input("Kam chceš hrát? "):
        try:
            nove_herni_pole = tah(pole, hracuv_index, symbol)
            return nove_herni_pole 
        except ValueError as error:
                print(error)

def piskvorky1d():
    herni_pole = "-" * 20
    if len(herni_pole) == 20 and isinstance(herni_pole, str) and match("^[-xo]*$", herni_pole) is not None:
        while hracuv_symbol := input("Jaký symbol chceš mít? x nebo o? "):
            if hracuv_symbol == "x":
                symbol_pocitace = "o"
                break
            elif hracuv_symbol == "o":
                symbol_pocitace = "x"
                break
            else:
                print("Dokud nezadáš 'x' nebo nezadáš 'o', tak se budu ptát dokola.")
        while True:
            try:
                herni_pole = tah_hrace(herni_pole, hracuv_symbol)
                if vyhodnot(herni_pole) != "-": break
                herni_pole = tah_pocitace(herni_pole, symbol_pocitace)
                if vyhodnot(herni_pole) != "-": break                
            except ValueError as error:
                print(error)
        if vyhodnot(herni_pole) == hracuv_symbol:
            print("Gratulace hráči, vyhrál jsi!")
        elif vyhodnot(herni_pole) == symbol_pocitace:
            print("Promiň hráči, vyhrál počítač. Ale i jemu gratulujeme.")
        elif vyhodnot(herni_pole) == "!":
            print("Remíza proti nejlepšímu počítači se taky počítá!")
    else:
        raise ValueError("Špatné hrací pole! Spusť hru znovu!")
