class ZakladniKalkulacka():
    def __init__(self):
        self.operatori = {'+': lambda x, y: x + y,
                          '-': lambda x, y: x - y,
                          '*': lambda x, y: x * y,
                          '/': lambda x, y: x / y}
        self.spusteni_operace()

    def nacteni_input1(self):
        while True:
            try:
                input1 = int(input("Zadej první èíslo: "))
                return input1
            except ValueError:
                print("Zadej èíslo èíslem brácho :-)")
    
    def nacteni_input2(self):
        while True:
            try:
                input2 = int(input("Zadej druhé èíslo: "))
                return input2
            except ValueError:
                print("Zadej èíslo èíslem brácho :-)")
                
    def nacteni_operace(self):
        while operace := input("Zadej operaci: "):
            try:
                self.operatori[operace]
                return operace
            except KeyError:
                print(f'Musíš zadat {str(self.operatori.keys())[11:-2]}, nic jiného program nezná.')

    def spusteni_operace(self):
        cislo1, cislo2 = self.nacteni_input1(), self.nacteni_input2()
        operace = self.nacteni_operace()
        try:
            print(f"Výsledek je: {self.operatori[operace](cislo1, cislo2)}")
        except ZeroDivisionError:
            print("Nulou dìlit nelze! Takže výsledek nedostaneš!")


if __name__ == "__main__":
    zakladnikalkulacka = ZakladniKalkulacka()