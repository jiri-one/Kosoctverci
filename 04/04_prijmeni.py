def vyhodnot_gender(vstup):
    if vstup[-1:] == "á":
        return f"{vstup}. Ty budeš asi holka, že?"
    else:
        return f"{vstup}. Ty budeš asi kluk, že?"

print(vyhodnot_gender("Nováková"))
print(vyhodnot_gender("Novák"))
print(vyhodnot_gender("Nevimjaká"))
