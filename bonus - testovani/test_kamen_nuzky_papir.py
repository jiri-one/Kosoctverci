from kamen_nuzky_papir import vyhodnot

def test_vyhodnot():
	assert vyhodnot("kámen", "nůžky") == "kámen"
	assert vyhodnot("papír", "nůžky") == "nůžky"
	assert vyhodnot("papír", "kámen") == "papír"