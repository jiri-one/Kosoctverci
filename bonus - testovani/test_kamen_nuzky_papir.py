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
def test_vyhodnot(tah_hrace, tah_pocitace, ocekavany_vysledek):
    assert vyhodnot(tah_hrace, tah_pocitace) == ocekavany_vysledek

# NEGATIVNÍNÍ TESTY

# tady všechny vstupy špatně
@pytest.mark.parametrize("tah_hrace", ("metal", "papir", "kravovina"))
@pytest.mark.parametrize("tah_pocitace", ("chmm", "juchjuch", "nuzky"))
def test2_vyhodnot(tah_hrace, tah_pocitace):
    with pytest.raises(ValueError):
        vyhodnot(tah_hrace, tah_pocitace)

# tady všechny vstupy dobře
@pytest.mark.parametrize("tah_hrace", ("kámen", "nůžky", "papír"))
# tady všechny vstupy špatně
@pytest.mark.parametrize("tah_pocitace", ("chmm", "nevim", "next"))
def test3_vyhodnot(tah_hrace, tah_pocitace):
    with pytest.raises(ValueError):
        vyhodnot(tah_hrace, tah_pocitace)
        
# tady všechny vstupy dobře
@pytest.mark.parametrize("tah_pocitace", ("kámen", "nůžky", "papír"))
# tady všechny vstupy špatně
@pytest.mark.parametrize("tah_hrace", ("chmm", "nevim", "next"))
def test3_vyhodnot(tah_hrace, tah_pocitace):
    with pytest.raises(ValueError):
        vyhodnot(tah_hrace, tah_pocitace)

