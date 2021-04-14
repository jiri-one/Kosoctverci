from random import randint
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

#print(tah("----x-----o---------", 5, "x"))
nove_hraci_pole = "----x-----o---------"
for _ in range(100):
    try:
        nove_hraci_pole = tah(nove_hraci_pole, randint(0, 19), "x")
        nove_hraci_pole = tah(nove_hraci_pole, randint(0, 19), "o")
    except ValueError as error:
        print(error)
    if nove_hraci_pole == None:
        break