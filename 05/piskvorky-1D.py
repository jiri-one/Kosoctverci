from re import match
from random import randint

def vyhodnot(hraci_pole):
    "Vyhodnotí stav hracího pole a vrátí vítěze, remízu nebo řekne, že hra ještě neskončila"
    if len(hraci_pole) == 20 and isinstance(hraci_pole, str) and match("^[-xo]*$", hraci_pole) is not None:
        if "xxx" in hraci_pole:
            return "x"
        elif "ooo" in hraci_pole:
            return "o"
        elif "-" not in hraci_pole:
            return "!"
        else:
            return "-"
    else:
        raise ValueError("Špatné hrací pole! Spusť hru znovu!")


def tah(hraci_pole, index, symbol):
    """Vrátí herní pole s daným symbolem umístěným na danou pozici:
    `hraci_pole` je herní pole, na které se hraje.
    `index` je číslo políčka. Čísluje se od nuly, prostě standardní index.
    `symbol` může být 'x' nebo 'o', podle toho jestli je tah za křížky
    nebo za kolečka.
    """
    try:
        index = int(index)
    except ValueError:
        raise ValueError("Zádávej pouze čísla!")
    else:
        if index not in (range(20)):
            raise ValueError("Tam nejde hrát!")
        elif hraci_pole[index] != "-":
            raise ValueError("Obsazeno!")
        elif symbol != "x" and symbol != "o":
            raise ValueError("Špatný symbol! pouze 'x' nebo 'o'")
        else:
            nove_herni_pole = hraci_pole[:index] + symbol + hraci_pole[index+1:]
            print(f"Nový stav hry je: {nove_herni_pole}")
            return nove_herni_pole

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
             
def tah_pocitace(hraci_pole, symbol):
    """Vrátí herní pole se zaznamenaným tahem počítače:
    `pole` je herní pole, na které se hraje.
    `symbol` může být 'x' nebo 'o', podle toho jestli hráč hraje za křížky
    nebo za kolečka.
    """
    while index_pocitace := randint(0,19):
        if hraci_pole[index_pocitace] == "-":
            nove_herni_pole = hraci_pole[:index_pocitace] + symbol + hraci_pole[index_pocitace+1:]
            print(f"Nový stav hry po tahu počítače je: {nove_herni_pole}")
            return nove_herni_pole

def piskvorky1d():
    herni_pole = "-" * 20
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
            break
    if vyhodnot(herni_pole) == hracuv_symbol:
        print("Gratulace hráči, vyhrál jsi!")
    elif vyhodnot(herni_pole) == symbol_pocitace:
        print("Promiň hráči, vyhrál počítač. Ale i jemu gratulujeme.")
    elif vyhodnot(herni_pole) == "!":
        print("Remíza proti nejlepšímu počítači se taky počítá!")
    
        
piskvorky1d()
#tah_hrace("----x-----o---------", "x")