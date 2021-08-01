from random import choice

slova = ["kámen", "nůžky", "papír"]
korekce_hrace = "Tenhle program zná jen: kámen, nůžky, papír a nebo konec."

def vyhodnot(tah_hrace, tah_pocitace):
    volby = {tah_hrace: ("hráč", "a") , tah_pocitace: ("počítač", "b")}
    if tah_hrace in slova and tah_pocitace in slova:
        # vyhodnocení případné remízy
        if tah_hrace == tah_pocitace:
            vitez = None
            finalni_hlaska = "Remíza!"
        # vyhodnocení vítěze
        if "kámen" in volby.keys() and "nůžky" in volby.keys():
            vitez = volby["kámen"][1]
            finalni_hlaska = f"""Kámen tupí nůžky! Vyhrává {volby["kámen"][0]}."""
        elif "nůžky" in volby.keys() and "papír" in volby.keys():
            vitez = volby["nůžky"][1]
            finalni_hlaska = f"""Nůžky sříhají papír! Vyhrává {volby["nůžky"][0]}."""
        elif "papír" in volby.keys() and "kámen" in volby.keys():
            vitez = volby["papír"][1]
            finalni_hlaska = f"""Papír zabalí kámen! Vyhrává {volby["papír"][0]}."""
        return vitez, finalni_hlaska
    else: # vstup je špatný, není v proměnné slova
        raise ValueError

def hra():
    while tah_hrace := input("Jaký volíš tah? "):
        try:
            if tah_hrace == "konec":
                print("Chápu, tahle hra je nuda. Končíme!")
                break
            else:
                tah_pocitace = choice(slova)
                vitez, finalni_hlaska = vyhodnot(tah_hrace, tah_pocitace)
                print(finalni_hlaska)
        except ValueError:
            print(korekce_hrace)

if __name__ == "__main__":
    hra()
    



