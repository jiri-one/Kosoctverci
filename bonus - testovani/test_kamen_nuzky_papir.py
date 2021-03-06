# this file contains only test functions

from kamen_nuzky_papir import vyhodnot
from helpers import fake_game

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

def test_hlasky_after_game():
    """We are going to test result from our fake functions."""
    hlasky = fake_game()
    assert hlasky == ["Papír zabalí kámen! Vyhrává hráč.",
                      "Remíza!",
                      "Papír zabalí kámen! Vyhrává počítač.",
                      "Tenhle program zná jen: kámen, nůžky, papír a nebo konec.",
                      "Chápu, tahle hra je nuda. Končíme!"]