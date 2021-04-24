import ai_jiri
from piskvorky import vyhodnot
from random import choice

def urci_viteznou_barvu(cerveni, modri, vitez):
    if cerveni == vitez:
        return "Červení"
    elif modri == vitez:
        return "Modří"
    
def zapas_robotu():
    herni_pole = "-" * 20
    symboly = ["x", "o"]
    cerveni = choice(symboly)
    symboly.remove(cerveni)
    modri = symboly[0]
    while True:
        try:
            herni_pole = ai_jiri.tah_pocitace(herni_pole, 'x')
            if vyhodnot(herni_pole) != "-": break  
            herni_pole = ai_jiri.tah_pocitace(herni_pole, 'o')
            if vyhodnot(herni_pole) != "-": break                
        except ValueError as error:
            print(error)
    if vyhodnot(herni_pole) == "!":
        print("Remíza dvou počítačů :D")
        return 0, 0
    else:
        vitezna_barva = urci_viteznou_barvu(cerveni, modri, vyhodnot(herni_pole))
        print(f"Tentokrát vyhráli {vitezna_barva}!")
        if vitezna_barva == "Červení":
            return 1, 0
        elif vitezna_barva == "Modří":
            return 0, 1
        

zapas_robotu()

body_cerveni, body_modri = 0, 0
for zapas in range(100):
    novy_bod_cerveni, novy_bod_modri = zapas_robotu()
    body_cerveni = body_cerveni + novy_bod_cerveni
    body_modri = body_modri + novy_bod_cerveni

print(f"Červení dosáhli na score {body_cerveni}. Gratulujeme.")
print(f"Modří dosáhli na score {body_modri}. Gratulujeme.")
