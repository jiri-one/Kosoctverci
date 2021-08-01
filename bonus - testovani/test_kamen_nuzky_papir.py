from kamen_nuzky_papir import vyhodnot
import pytest

# NORMÁLNÍ TESTY

# test správných výsledků
@pytest.mark.parametrize(
    ("tah_hrace", "tah_pocitace", "ocekavany_vysledek", "ocekavana_hlaska"), 
    [
        ("kámen", "nůžky", "a", "Kámen tupí nůžky! Vyhrává hráč."),
        ("nůžky", "kámen", "b", "Kámen tupí nůžky! Vyhrává počítač."),
        ("nůžky", "papír", "a", "Nůžky sříhají papír! Vyhrává hráč."),
        ("papír", "nůžky", "b", "Nůžky sříhají papír! Vyhrává počítač."),
        ("papír", "kámen", "a", "Papír zabalí kámen! Vyhrává hráč."),
        ("kámen", "papír", "b", "Papír zabalí kámen! Vyhrává počítač."),
        ("kámen", "kámen", None, "Remíza!"),
        ("papír", "papír", None, "Remíza!"),
        ("nůžky", "nůžky", None, "Remíza!")
    ])
def test_all_good_options(tah_hrace, tah_pocitace, ocekavany_vysledek, ocekavana_hlaska):
    """We are going to test function vyhodnot with all possible good inputs"""
    vitez, finalni_hlaska = vyhodnot(tah_hrace, tah_pocitace)
    assert vitez == ocekavany_vysledek
    assert finalni_hlaska == ocekavana_hlaska

# NEGATIVNÍNÍ TESTY

# tady všechny vstupy špatně
@pytest.mark.parametrize("tah_hrace", ("metal", "papir", "kravovina"))
@pytest.mark.parametrize("tah_pocitace", ("chmm", "juchjuch", "nuzky"))
def test_bad_inputs(tah_hrace, tah_pocitace):
    """We are going to test function vyhodnot with some bad inputs"""
    with pytest.raises(ValueError):
        vyhodnot(tah_hrace, tah_pocitace)

# tady všechny vstupy dobře
@pytest.mark.parametrize("tah_hrace", ("kámen", "nůžky", "papír"))
# tady všechny vstupy špatně
@pytest.mark.parametrize("tah_pocitace", ("chmm", "nevim", "next"))
def test_bad_ai_inputs(tah_hrace, tah_pocitace):
    """We are going to test function vyhodnot with combination of bad and good inputs"""
    with pytest.raises(ValueError):
        vyhodnot(tah_hrace, tah_pocitace)
        
# tady všechny vstupy dobře
@pytest.mark.parametrize("tah_pocitace", ("kámen", "nůžky", "papír"))
# tady všechny vstupy špatně
@pytest.mark.parametrize("tah_hrace", ("chmm", "nevim", "next"))
def test_bad_player_inputs(tah_hrace, tah_pocitace):
    """We are going to test function vyhodnot with another combination of bad and good inputs"""
    with pytest.raises(ValueError):
        vyhodnot(tah_hrace, tah_pocitace)

odpovedi_naopak = ["konec", "kravovina", "kámen", "nůžky", "papír"]
def falesny_input(otazka):
    return odpovedi_naopak.pop()

volby_knp = ["kámen", "nůžky", "nůžky"]
def falesny_choice(pocitac_voli_z):
    return volby_knp.pop()

hlasky = []
def falesny_print(hlaska):
    hlasky.append(hlaska)

