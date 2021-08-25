# file with helpers (function which will help with testing)

from kamen_nuzky_papir import hra

def fake_game():
    """Only help function to run fake game and get some result which we are going to test."""
    # some fake functions for our main test of fake game
    odpovedi_naopak = ["konec", "kravovina", "kámen", "nůžky" , "papír"]
    def falesny_input(otazka):
        return odpovedi_naopak.pop()
    
    volby_knp = ["", "", "papír", "nůžky", "kámen"]
    def falesny_choice(pocitac_voli_z):
        return volby_knp.pop()

    hlasky = []
    def falesny_print(hlaska):
        hlasky.append(hlaska)    
    
    hra(print=falesny_print, input=falesny_input, choice=falesny_choice)
    
    return hlasky