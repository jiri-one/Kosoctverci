input1 = int(input("Zadej první číslo: "))
input2 = int(input("Zadej druhé číslo: "))
operace = input("Zadej operaci: ")

if operace == "+":
    print("Výsledek sčítání je: ", input1 + input2)
elif operace == "-":
    print("Výsledek odčítání je: ", input1 - input2)
elif operace == "*":
    print("Výsledek násobení je: ", input1 * input2)
elif operace == "/":
    print("Výsledek dělení je: ", input1 / input2)
else:
    print("Neznámá operace.")
