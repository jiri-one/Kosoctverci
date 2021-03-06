
class Figurka:
    def __init__(self, strana, druh):
        self.strana = strana
        self.druh = druh

    def __str__(self):
        """Textový popis figurky"""
        return f'"{self.strana} {self.druh}"'

    def over_tah(self, sachovnice, puvodni_pozice, nova_pozice):
        """Zkontroluje, že se tato figurka může daným způsobem pohnout

        Když tah nejde provést, tahle metoda způsobí ValueError.

        sachovnice: Šachovnice, na které se figurka hýbe
        puvodni_pozice: Dvojice (radek, sloupec): kde figurka právě je
        nova_pozice: Dvojice (radek, sloupec): kam figurka má jít

        Řádky a sloupce jsou čísla 0-7.
        """

        # Pokud se figurka nehýbe, nejde o tah
        if puvodni_pozice == nova_pozice:
            raise ValueError('Nehýbe se')

        # Ven z šachovnice se nedá táhnout
        radek, sloupec = nova_pozice
        if radek < 0 or sloupec < 0 or radek >= 8 or sloupec >= 8:
            raise ValueError('Venku z šachovnice')

        # Taky se nedá táhnout na figurku stejné barvy
        figurka = sachovnice.figurka_na(nova_pozice)
        if figurka != None and figurka.strana == self.strana:
            raise ValueError(f'Blokuje {figurka} stejné barvy')

    def tahni(self, sachovnice, puvodni_pozice, nova_pozice):
        sachovnice.tahni(puvodni_pozice, nova_pozice)
        


class Vez(Figurka):
    def __init__(self, strana):
        super().__init__(strana, 'vez')
        self.prvni_tah = 1 # !!! pridal jsem pouze tohle !!! a ještě jsem "supernul" metodu tahni

    def over_tah(self, sachovnice, puvodni_pozice, nova_pozice):
        # (viz dokumentační řetězec v nadtřídě.)

        # Nejdřív proveď ověření, která jsou společné všem figurkám
        super().over_tah(sachovnice, puvodni_pozice, nova_pozice)

        # Rozložení pozic (radek, sloupec) na čísla
        puvodni_radek, puvodni_sloupec = puvodni_pozice
        novy_radek, novy_sloupec = nova_pozice

        if puvodni_radek == novy_radek:
            # Věž se pohybuje "horizontálně", po řádku.
            # Potřebujeme `range` s čísly sloupců, které tím věž přeskočí.
            if puvodni_sloupec < novy_sloupec:
                # věž jde doprava
                preskocene_sloupce = range(puvodni_sloupec+1, novy_sloupec)
            else:
                # věž jde doleva
                preskocene_sloupce = range(novy_sloupec+1, puvodni_sloupec)
            # Na žádném z přeskočených políček nesmí být figurka:
            for sloupec in preskocene_sloupce:
                testovana_pozice = puvodni_radek, sloupec
                blokujici = sachovnice.figurka_na(testovana_pozice)
                if blokujici != None:
                    raise ValueError(f'V cestě je {blokujici}')
        elif puvodni_sloupec == novy_sloupec:
            # Podobně pohyb "vertikálně"
            if puvodni_radek < novy_radek:
                preskocene_radky = range(puvodni_radek+1, novy_radek)
            else:
                preskocene_radky = range(novy_radek+1, puvodni_radek)
            for radek in preskocene_radky:
                testovana_pozice = radek, puvodni_sloupec
                blokujici = sachovnice.figurka_na(testovana_pozice)
                if blokujici != None:
                    raise ValueError(f'V cestě je {blokujici}')
        else:
            raise ValueError(f'Musí se hýbat po řádku nebo sloupci')
    # !!! tedy tuhle metodu !!!    
    def tahni(self, sachovnice, puvodni_pozice, nova_pozice):
        super().tahni(sachovnice, puvodni_pozice, nova_pozice) 
        self.prvni_tah = 0

class Kun(Figurka):
    def __init__(self, strana):
        super().__init__(strana, 'kun')

    def over_tah(self, sachovnice, puvodni_pozice, nova_pozice):
        # (viz dokumentační řetězec v nadtřídě.)

        # Nejdřív proveď ověření, která jsou společné všem figurkám
        super().over_tah(sachovnice, puvodni_pozice, nova_pozice)

        # Rozložení pozic (radek, sloupec) na čísla
        puvodni_radek, puvodni_sloupec = puvodni_pozice
        novy_radek, novy_sloupec = nova_pozice

        vzdalenost_v_radcich = abs(novy_radek - puvodni_radek)
        vzdalenost_ve_sloupcich = abs(novy_sloupec - puvodni_sloupec)        
        if ((vzdalenost_v_radcich == 2 and vzdalenost_ve_sloupcich == 1)
        or (vzdalenost_v_radcich == 1 and vzdalenost_ve_sloupcich == 2)):
            pass
        else:
            raise ValueError(f'Musí se hýbat pouze po trajektorii písmene L a nožička musí být 2 pole dlouhá :-)')
        
class Kral(Figurka):
    def __init__(self, strana):
        super().__init__(strana, 'kral')
        self.prvni_tah = 1
        self.mala_rosada_bilych = 0
        self.velka_rosada_bilych = 0
        self.mala_rosada_cernych = 0
        self.velka_rosada_cernych = 0

    def over_tah(self, sachovnice, puvodni_pozice, nova_pozice):
        # (viz dokumentační řetězec v nadtřídě.)

        # Nejdřív proveď ověření, která jsou společné všem figurkám
        super().over_tah(sachovnice, puvodni_pozice, nova_pozice)

        # Rozložení pozic (radek, sloupec) na čísla
        puvodni_radek, puvodni_sloupec = puvodni_pozice
        novy_radek, novy_sloupec = nova_pozice
        
        self.pole_rosady = [] 
        try: # musím ošetřit vyjímku, protože už tam taky možná žádná věž nestojí ... (jsou i jiné způsoby, vím to :-))
            # malá rošáda bílých
            if (sachovnice.hrac_na_tahu == "bily" and # zapiseme souradnice rosady pouze tehdy, kdyz je bily na tahu
                str(sachovnice.figurka_na((0,7))) == '"bily vez"' and # vez je spravne barvy (neni v zasade nutne kontrolovat)
                sachovnice.figurka_na((0,7)).prvni_tah == 1 and # a jeste nikdy se nepohnula (to je nutne kontrolovat :-D)
                self.prvni_tah == 1 and # kral se jeste nepohnul
                sachovnice.figurka_na((0,6)) == None and # a nic nestoji krali v ceste smerem k vezi
                sachovnice.figurka_na((0,5)) == None ): # a fakt jako vubec nic :)
                self.pole_rosady.append((0,6)) # tak pridej pole, kam se kral muze hnout do self.pole_rosady
    
            # velká rošáda bílých
            if (sachovnice.hrac_na_tahu == "bily" and # zapiseme souradnice rosady pouze tehdy, kdyz je bily na tahu
                str(sachovnice.figurka_na((0,0))) == '"bily vez"' and # vez je spravne barvy (neni v zasade nutne kontrolovat)
                sachovnice.figurka_na((0,0)).prvni_tah == 1 and # a jeste nikdy se nepohnula (to je nutne kontrolovat :-D)          
                self.prvni_tah == 1 and # kral se jeste nepohnul
                sachovnice.figurka_na((0,3)) == None and # a nic nestoji krali v ceste smerem k druhe vezi
                sachovnice.figurka_na((0,2)) == None and # a fakt jako vubec nic :)
                sachovnice.figurka_na((0,1)) == None ): # a fakt jako vubec, ale vubec, nic :)
                self.pole_rosady.append((0,2)) # tak pridej pole, kam se kral muze hnout do self.pole_rosady
            
            # malá rošáda černých
            if (sachovnice.hrac_na_tahu == "cerny" and # zapiseme souradnice rosady pouze tehdy, kdyz je cerny na tahu
                str(sachovnice.figurka_na((7,7))) == '"cerny vez"' and # vez je spravne barvy (neni v zasade nutne kontrolovat)
                sachovnice.figurka_na((7,7)).prvni_tah == 1 and # a jeste nikdy se nepohnula (to je nutne kontrolovat :-D) 
                self.prvni_tah == 1 and # kral se jeste nepohnul
                sachovnice.figurka_na((7,6)) == None and # a nic nestoji krali v ceste smerem k vezi
                sachovnice.figurka_na((7,5)) == None ): # a fakt jako vubec nic :)
                self.pole_rosady.append((7,6)) # tak pridej pole, kam se kral muze hnout do self.pole_rosady
    
            # velká rošáda černých
            if (sachovnice.hrac_na_tahu == "cerny" and # zapiseme souradnice rosady pouze tehdy, kdyz je cerny na tahu
                str(sachovnice.figurka_na((7,0))) == '"cerny vez"' and # vez je spravne barvy (neni v zasade nutne kontrolovat)
                sachovnice.figurka_na((7,7)).prvni_tah == 1 and # a jeste nikdy se nepohnula (to je nutne kontrolovat :-D) 
                self.prvni_tah == 1 and # kral se jeste nepohnul
                sachovnice.figurka_na((7,3)) == None and # a nic nestoji krali v ceste smerem k druhe vezi
                sachovnice.figurka_na((7,2)) == None and # a fakt jako vubec nic :)
                sachovnice.figurka_na((7,1)) == None ):# a fakt jako vubec, ale vubec, nic :)
                self.pole_rosady.append((7,2)) # tak pridej pole, kam se kral muze hnout do self.pole_rosady 
        except AttributeError:
            pass

        if (abs(novy_radek - puvodni_radek) > 1 or abs(novy_sloupec - puvodni_sloupec) > 1) and nova_pozice not in self.pole_rosady:
            raise ValueError(f'Král dál než o jedno políčko nemůže. Vyjímkou je rošáda.')
    
    def tahni(self, sachovnice, puvodni_pozice, nova_pozice):
        super().tahni(sachovnice, puvodni_pozice, nova_pozice) 
        if nova_pozice in self.pole_rosady and self.prvni_tah == 1:
            if nova_pozice == (0,6):
                sachovnice.figurka_na((0,7)).tahni(sachovnice,(0,7),(0,5))            
            elif nova_pozice == (0,2):
                sachovnice.figurka_na((0,0)).tahni(sachovnice,(0,0),(0,3))  
            elif nova_pozice == (7,6):
                sachovnice.figurka_na((7,7)).tahni(sachovnice,(7,7),(7,5)) 
            elif nova_pozice == (7,2):
                sachovnice.figurka_na((7,0)).tahni(sachovnice,(7,0),(7,3)) 
        self.prvni_tah = 0
        self.pole_rosady = []
        

class Strelec(Figurka):
    def __init__(self, strana):
        super().__init__(strana, 'strelec')

    def over_tah(self, sachovnice, puvodni_pozice, nova_pozice):
        # (viz dokumentační řetězec v nadtřídě.)

        # Nejdřív proveď ověření, která jsou společné všem figurkám
        super().over_tah(sachovnice, puvodni_pozice, nova_pozice)

        # Rozložení pozic (radek, sloupec) na čísla
        puvodni_radek, puvodni_sloupec = puvodni_pozice
        novy_radek, novy_sloupec = nova_pozice
        citac_radku = 1 # jde nahoru
        citac_sloupce = 1 # jde vpravo
        if abs(novy_radek - puvodni_radek) == abs(novy_sloupec - puvodni_sloupec):
            if puvodni_radek > novy_radek: # jde dolu
                citac_radku = -1
            if puvodni_sloupec > novy_sloupec: # jde vlevo
                citac_sloupce = -1            
            
            for radek, sloupec in zip(range(puvodni_radek+citac_radku, novy_radek,citac_radku), range(puvodni_sloupec+citac_sloupce,novy_sloupec,citac_sloupce)):
                    testovana_pozice = radek, sloupec
                    print(testovana_pozice)
                    blokujici = sachovnice.figurka_na(testovana_pozice)
                    if blokujici != None:
                        raise ValueError(f'V cestě je {blokujici}') 
        else:
            raise ValueError(f'Střelec může vždy pouze diagonálně.') 

class Dama(Figurka):
    def __init__(self, strana):
        super().__init__(strana, "dama")

    def over_tah(self, sachovnice, puvodni_pozice, nova_pozice):
        # (viz dokumentační řetězec v nadtřídě.)
        # Nejdřív proveď ověření, která jsou společné všem figurkám
        super().over_tah(sachovnice, puvodni_pozice, nova_pozice)
        # Rozložení pozic (radek, sloupec) na čísla
        puvodni_radek, puvodni_sloupec = puvodni_pozice
        novy_radek, novy_sloupec = nova_pozice
        
        if puvodni_radek == novy_radek:
            # Věž se pohybuje "horizontálně", po řádku.
            # Potřebujeme `range` s čísly sloupců, které tím věž přeskočí.
            if puvodni_sloupec < novy_sloupec:
                # věž jde doprava
                preskocene_sloupce = range(puvodni_sloupec+1, novy_sloupec)
            else:
                # věž jde doleva
                preskocene_sloupce = range(novy_sloupec+1, puvodni_sloupec)
            # Na žádném z přeskočených políček nesmí být figurka:
            for sloupec in preskocene_sloupce:
                testovana_pozice = puvodni_radek, sloupec
                blokujici = sachovnice.figurka_na(testovana_pozice)
                if blokujici != None:
                    raise ValueError(f'V cestě je {blokujici}')
        elif puvodni_sloupec == novy_sloupec:
            # Podobně pohyb "vertikálně"
            if puvodni_radek < novy_radek:
                preskocene_radky = range(puvodni_radek+1, novy_radek)
            else:
                preskocene_radky = range(novy_radek+1, puvodni_radek)
            for radek in preskocene_radky:
                testovana_pozice = radek, puvodni_sloupec
                blokujici = sachovnice.figurka_na(testovana_pozice)
                if blokujici != None:
                    raise ValueError(f'V cestě je {blokujici}')
                citac_radku = 1 # jde nahoru
                citac_sloupce = 1 # jde vpravo
        
        elif abs(novy_radek - puvodni_radek) == abs(novy_sloupec - puvodni_sloupec):
            citac_radku = 1 # jde nahoru
            citac_sloupce = 1 # jde vpravo            
            if novy_radek - puvodni_radek < 0: # jde dolu
                citac_radku = -1
            if novy_sloupec - puvodni_sloupec < 0: # jde vlevo
                citac_sloupce = -1            
    
            for radek, sloupec in zip(range(puvodni_radek+citac_radku, novy_radek,citac_radku), range(puvodni_sloupec+citac_sloupce,novy_sloupec,citac_sloupce)):
                testovana_pozice = radek, sloupec
                print(testovana_pozice)
                blokujici = sachovnice.figurka_na(testovana_pozice)
                if blokujici != None:
                    raise ValueError(f'V cestě je {blokujici}')         
        else:
            raise ValueError(f'Musí se hýbat po řádku nebo sloupci nebo diagonálně')

class Pesec(Figurka):
    def __init__(self, strana):
        super().__init__(strana, 'pesec')
        self.prvni_tah = 1
        
    def over_tah(self, sachovnice, puvodni_pozice, nova_pozice):
        # (viz dokumentační řetězec v nadtřídě.)
        # Nejdřív proveď ověření, která jsou společné všem figurkám
        super().over_tah(sachovnice, puvodni_pozice, nova_pozice)
        # Rozložení pozic (radek, sloupec) na čísla
        puvodni_radek, puvodni_sloupec = puvodni_pozice
        novy_radek, novy_sloupec = nova_pozice
        
        nepratele = []
        if self.strana == "bily":
            for nepratelske_koordinaty in [(puvodni_radek+1, puvodni_sloupec+1), 
                                           (puvodni_radek+1, puvodni_sloupec-1)]:
                potencionalni_nepritel = sachovnice.figurka_na(nepratelske_koordinaty)
                if potencionalni_nepritel:
                    if potencionalni_nepritel.strana != self.strana:
                        nepratele.append(nepratelske_koordinaty)
        else: # self.strana == "cerny"
            for nepratelske_koordinaty in [(puvodni_radek-1, puvodni_sloupec+1),
                                           (puvodni_radek-1, puvodni_sloupec-1)]:
                potencionalni_nepritel = sachovnice.figurka_na(nepratelske_koordinaty)
                if potencionalni_nepritel:
                    if potencionalni_nepritel.strana != self.strana:
                        nepratele.append(nepratelske_koordinaty)            
        
        if nova_pozice in nepratele:
            pass
        elif sachovnice.figurka_na(nova_pozice) == None: 
            if puvodni_sloupec == novy_sloupec:
                if self.prvni_tah != 1:
                    if puvodni_radek + 1 != novy_radek and self.strana == "bily":
                        raise ValueError('Pesec muze jen po sloupci od jeden radek!')
                    elif puvodni_radek - 1 != novy_radek and self.strana == "cerny":
                        raise ValueError('Pesec muze jen po sloupci od jeden radek!')
                else: # self.prvni_tah == 1
                    if self.strana == "bily":
                        if novy_radek - puvodni_radek > 2 or novy_radek < puvodni_radek:
                            raise ValueError('Pesec muze jen po sloupci od jeden ci dva radky (pouze poprve) DOPREDU!')
                    else: # self.strana == "cerny"
                        if puvodni_radek - novy_radek > 2 or novy_radek > puvodni_radek:
                            raise ValueError('Pesec muze jen po sloupci od jeden ci dva radky (pouze poprve) DOPREDU!')                    
            else:
                raise ValueError('Pesec muze jen po sloupci.')
        else:
            raise ValueError('Sem pesec nesmi!')
    
    def tahni(self, sachovnice, puvodni_pozice, nova_pozice):
        super().tahni(sachovnice, puvodni_pozice, nova_pozice) 
        self.prvni_tah = 0
        novy_radek, _ = nova_pozice
        if novy_radek == 7 and self.strana == "bily":
            sachovnice.figurky.pop(nova_pozice)
            sachovnice.pridej(nova_pozice, Dama('bily'))
        if novy_radek == 0 and self.strana == "cerny":
            sachovnice.figurky.pop(nova_pozice)
            sachovnice.pridej(nova_pozice, Dama('cerny'))            
    
class Sachovnice:
    def __init__(self):
        self.vybrana_pozice = None
        self.hrac_na_tahu = "bily" # !!! ZMĚNA ZDE !!!

        self.figurky = {}
        
        self.pridej((0, 0), Vez('bily'))
        self.pridej((1, 1), Kun('bily'))
        self.pridej((1, 2), Strelec('bily'))
        self.pridej((1, 3), Dama('bily'))
        self.pridej((0, 4), Kral('bily'))
        self.pridej((1, 5), Strelec('bily'))
        self.pridej((1, 6), Kun('bily'))
        self.pridej((0, 7), Vez('bily'))

        self.pridej((2, 0), Pesec('bily'))
        self.pridej((2, 1), Pesec('bily'))
        self.pridej((2, 2), Pesec('bily'))
        self.pridej((2, 3), Pesec('bily'))
        self.pridej((2, 4), Pesec('bily'))
        self.pridej((2, 5), Pesec('bily'))
        self.pridej((2, 6), Pesec('bily'))
        self.pridej((2, 7), Pesec('bily'))

        self.pridej((5, 0), Pesec('cerny'))
        self.pridej((5, 1), Pesec('cerny'))
        self.pridej((5, 2), Pesec('cerny'))
        self.pridej((5, 3), Pesec('cerny'))
        self.pridej((5, 4), Pesec('cerny'))
        self.pridej((5, 5), Pesec('cerny'))
        self.pridej((5, 6), Pesec('cerny'))
        self.pridej((5, 7), Pesec('cerny'))

        self.pridej((7, 0), Vez('cerny'))
        self.pridej((6, 1), Kun('cerny'))
        self.pridej((6, 2), Strelec('cerny'))
        self.pridej((6, 3), Dama('cerny'))
        self.pridej((7, 4), Kral('cerny'))
        self.pridej((6, 5), Strelec('cerny'))
        self.pridej((6, 6), Kun('cerny'))
        self.pridej((7, 7), Vez('cerny'))

    def figurka_na(self, pozice):
        """Vrátí figurku na daných souřadnicích, nebo None"""
        radek, sloupec = pozice
        return self.figurky.get((radek, sloupec))

    def vrat_vybranou_figurku(self):
        """Vrátí figurku, která je právě vybraná (bude se hýbat)"""
        pozice = self.vybrana_pozice
        if pozice:
            return self.figurka_na(pozice)

    def pridej(self, pozice, figurka):
        """Přidá danou figurku na danou pozici

        Pokud je na cílové pozici jiná figurka, vyhodí ji.
        """
        self.figurky[pozice] = figurka

    def tahni(self, z, na):
        """Přemístí figurku z jedné pozice na druhou.

        Pokud je na cílové pozici jiná figurka, vyhodí ji.
        """
        figurka = self.figurky.pop(z)
        self.pridej(na, figurka)

    def muze_tahnout(self, nova_pozice):
        """Vrátí true, pokud právě vybraná figurka může táhnout na danou pozici
        """
        figurka = self.vrat_vybranou_figurku()
        if figurka == None:
            return False
        else:
            try:
                figurka.over_tah(self, self.vybrana_pozice, nova_pozice)
            except ValueError:
                return False
            else:
                return True

    def vyber_pozici(self, pozice):
        """Vybere figurku na dané pozici"""
        
        figurka = self.figurka_na(pozice)
        if figurka.strana != self.hrac_na_tahu: # !!! ZMĚNA ZDE !!!
            print("Nejsi na tahu") # !!! ZMĚNA ZDE !!!
            self.vybrana_pozice = None # !!! ZMĚNA ZDE !!!
        else: # !!! ZMĚNA ZDE !!!
            if figurka:
                self.vybrana_pozice = pozice
            else:
                self.vybrana_pozice = None

    def tahni_na_pozici(self, pozice):
        """Táhne vybranou figurkou na danou pozici"""

        if self.vybrana_pozice == None:
            return

        popis_z = popis_pozici(self.vybrana_pozice)
        popis_na = popis_pozici(pozice)

        figurka = self.figurka_na(self.vybrana_pozice)
        try:
            figurka.over_tah(self, self.vybrana_pozice, pozice)
        except ValueError as chyba:
            print(f'{figurka} nemůže na z {popis_z} na {popis_na}: {chyba}!')
        else:
            print(f'{figurka} jde z {popis_z} na {popis_na}!')
            figurka.tahni(self, self.vybrana_pozice, pozice)
            barvy = ["cerny", "bily"]  # !!! ZMĚNA ZDE !!!
            barvy.remove(self.hrac_na_tahu) # !!! ZMĚNA ZDE !!!
            self.hrac_na_tahu = barvy[0] # !!! ZMĚNA ZDE !!!
        self.vybrana_pozice = None
        

    def vykresli_se(self, kresli_obrazek):
        """Vykreslí šachovnici do Pyglet okýnka

        Jako argument bere funkce kresli_obrazek(figurka, radek, sloupec),
        která zajistí samotné vykreslení.
        """

        # Pozadí - střídavá políčka
        for radek in range(8):
            for sloupec in range(8):
                if (radek + sloupec) % 2 == 1:
                    kresli_obrazek('pole', radek, sloupec)
                else:
                    kresli_obrazek('pole2', radek, sloupec)

                # Označení možných tahů
                if self.vybrana_pozice:
                    kreslena_pozice = (radek, sloupec)
                    figurka = self.figurka_na(self.vybrana_pozice)
                    try:
                        figurka.over_tah(
                            self,
                            self.vybrana_pozice,
                            kreslena_pozice,
                        )
                    except ValueError as chyba:
                        pass
                    else:
                        kresli_obrazek('muze', radek, sloupec)

        # Figurky
        for (radek, sloupec), figurka in self.figurky.items():
            kresli_obrazek(f'{figurka.strana}_{figurka.druh}', radek, sloupec)

        # Výběr
        if self.vybrana_pozice:
            radek, sloupec = self.vybrana_pozice
            kresli_obrazek('vyber', radek, sloupec)

    def __str__(self):
        """Převede šachovnici na řetězec, který se dá vypsat"""

        # Tohle je variace na vypsání tabulky (úkoly typu "vypiš čtverec
        # poskládaný ze znaků X"), ale místo vypsání pomocí `print` se
        # spojí do jednoho řetězce.

        radky = ['   a b c d e f g h   ']
        for cislo_radku in range(8):
            radek = []
            for cislo_sloupce in range(8):
                pozice = cislo_radku, cislo_sloupce
                figurka = self.figurky.get(pozice)
                if figurka:
                    # Vybrání znaku pro danou figurku
                    jmena_figurek = 'kral dama vez strelec kun pesec'
                    d = jmena_figurek.split().index(figurka.druh)
                    s = 'bily cerny'.split().index(figurka.strana)
                    fig = "♔♕♖♗♘♙♚♛♜♝♞♟︎"[s * 6 + d]

                    radek.append(f' {fig}')
                else:
                    radek.append('  ')
            cislo = 8 - cislo_radku
            radky.append(f'{cislo} {"".join(radek)}  {cislo}')
        radky.append('   a b c d e f g h   ')
        return '\n'.join(radky)

round
def popis_pozici(pozice):
    """Popíše pozici pro lidi

    např:

    >>> popis_pozici(0, 0)
    'a1'

    """
    radek, sloupec = pozice
    return "abcdefgh"[sloupec] + "12345678"[radek]
