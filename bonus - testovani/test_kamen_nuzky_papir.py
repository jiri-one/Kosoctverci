from kamen_nuzky_papir import vyhodnot
import pytest

# NORMÁLNÍ TESTY

# test správných výsledků
@pytest.mark.parametrize(
    ("tah_hrace", "tah_pocitace", "ocekavany_vysledek"), 
    [
        ("kámen", "nůžky", "a"),
        ("nůžky", "kámen", "b"),
        ("nůžky", "papír", "a"),
        ("papír", "nůžky", "b"),
        ("papír", "kámen", "a"),
        ("kámen", "papír", "b"),
        ("kámen", "kámen", None),
        ("papír", "papír", None),
        ("nůžky", "nůžky", None)
    ])
def test_all_good_options(tah_hrace, tah_pocitace, ocekavany_vysledek):
    """We are going to test function vyhodnot with all possible good inputs"""
    vitez, finalni_hlaska = vyhodnot(tah_hrace, tah_pocitace)
    assert vitez == ocekavany_vysledek

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

