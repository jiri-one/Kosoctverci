from re import match

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
        raise ValueError("Špatné hrací pole!")
    
print(vyhodnot("----x-----o---------"))
