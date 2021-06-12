from random import choice

slova = ["kámen", "nůžky", "papír"]

def vyhodnot(tah_hrace, tah_pocitace):
    volby = {tah_hrace: ("hráč", "a") , tah_pocitace: ("počítač", "b")}
    if tah_hrace == tah_pocitace:
        print("Remíza!") # tady předpokládám, že je return None
    if "kámen" in volby.keys() and "nůžky" in volby.keys():
        print(f"""Kámen tupí nůžky! Vyhrává {volby["kámen"][0]}.""")
        return volby["kámen"][1] # přidáno kvůli testování
    elif "nůžky" in volby.keys() and "papír" in volby.keys():
        print(f"""Nůžky sříhají papír! Vyhrává {volby["nůžky"][0]}.""")
        return volby["nůžky"][1] # přidáno kvůli testování
    elif "papír" in volby.keys() and "kámen" in volby.keys():
        print(f"""Papír zabalí kámen! Vyhrává {volby["papír"][0]}.""")
        return volby["papír"][1] # přidáno kvůli testování

if __name__ == "__main__":
    while tah_hrace := input("Jaký volíš tah? "):
        tah_pocitace = choice(slova)
        if tah_hrace in slova:
            vyhodnot(tah_hrace, tah_pocitace)
        elif tah_hrace == "konec":
            print("Chápu, tahle hra je nuda. Končíme!")
            break
        else:
            print("Tenhle program zná jen: kámen, nůžky, papír a nebo konec.")



