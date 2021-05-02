from random import shuffle

def vytvor_balicek():
    hodnoty = [str(x) for x in range(2,11)] + ['J', 'Q', 'K', 'A']
    barvy = ['♥', '♦', '♠', '♣']    
    karty = []
    for barva in barvy:
        for hodnota in hodnoty:
            karty.append((hodnota, barva))
    shuffle(karty)
    return karty

print(vytvor_balicek())
