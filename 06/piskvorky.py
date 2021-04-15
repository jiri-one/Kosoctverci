from util import tah

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

