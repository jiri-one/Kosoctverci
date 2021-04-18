from random import shuffle

hodnoty = [str(x) for x in range(2,11)] + ['J', 'Q', 'K', 'A']
barvy = ['♥', '♦', '♠', '♣']

def vytvor_balicek():
    karty = []
    for barva in barvy:
        for hodnota in hodnoty:
            karty.append((hodnota, barva))
    shuffle(karty)
    return karty

vytvor_balicek()
vytvor_balicek()