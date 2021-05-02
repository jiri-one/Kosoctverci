# říkal jsem si, že tenhle program chce prostě zkrátit ;)

from random import choice

slova = ["kámen", "nůžky", "papír"]

def vitez(tah_hrace, tah_pocitace):
    volby = {tah_hrace: "hráč" , tah_pocitace: "počítač"}
    if tah_hrace == tah_pocitace:
        print("Remíza!")
    if "kámen" in volby.keys() and "nůžky" in volby.keys():
        print(f"""Kámen tupí nůžky! Vyhrává {volby["kámen"]}.""")
    elif "nůžky" in volby.keys() and "papír" in volby.keys():
        print(f"""Nůžky sříhají papír! Vyhrává {volby["nůžky"]}.""")
    elif "papír" in volby.keys() and "kámen" in volby.keys():
        print(f"""Papír zabalí kámen! Vyhrává {volby["papír"]}.""")    

while tah_hrace := input("Jaký volíš tah? "):
    tah_pocitace = choice(slova)
    if tah_hrace in slova:
        vitez(tah_hrace, tah_pocitace)
    elif tah_hrace == "konec":
        print("Chápu, tahle hra je nuda. Končíme!")
        break
    else:
        print("Tenhle program zná jen: kámen, nůžky, papír a nebo konec.")



