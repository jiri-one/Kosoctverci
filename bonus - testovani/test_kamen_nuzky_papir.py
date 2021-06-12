from kamen_nuzky_papir import vyhodnot

# normální testy
def test_vyhodnot():
	assert vyhodnot("kámen", "nůžky") == "a"
	assert vyhodnot("nůžky", "kámen") == "b"
	assert vyhodnot("nůžky", "papír") == "a"
	assert vyhodnot("papír", "nůžky") == "b"
	assert vyhodnot("papír", "kámen") == "a"
	assert vyhodnot("kámen", "papír") == "b"
	assert vyhodnot("kámen", "kámen") == None
	assert vyhodnot("papír", "papír") == None
	assert vyhodnot("nůžky", "nůžky") == None

# negativní testy
def test2_vyhodnot():
	assert vyhodnot("papir", "metal") == None
	assert vyhodnot("papír", "metal") == None
	assert vyhodnot("metal", "nůžky") == None