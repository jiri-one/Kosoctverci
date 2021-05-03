def vypis_slovnik(slovnik):
    for klic, hodnota in slovnik.items():
        print(f"Klíč {klic}, hodnota {hodnota}")
        
vypis_slovnik(mocniny(4))