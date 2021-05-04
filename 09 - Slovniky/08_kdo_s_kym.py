from random import choice

def ziskej_odpovedi():
    print("""
    Zdar borče či borko (heh, Nelí asi, což? ;-)),
    potřebuji od Tebe pár odpovědí.
    Můžeš napsat odpovědí kolik chceš. Jakmile napíšeš "konec",
    tak přecházíš k další otázce nebo fakt končíme a jdeme k vyhonocení.\n""")
    otazky = {"Kdo?": [], "S kým?": [], "Co dělali?": [], "Kde?": [], "Kdy?": [], "Proč?": []}
    for otazka in otazky:
        odpoved = ""
        while True:
            odpoved = input(f"Takže! {otazka} ")
            if odpoved == "" or (len(otazky[otazka]) == 0 and odpoved == "konec"):
                print("Musíš odpověďět!")
            elif odpoved == "konec":
                break
            else:
                otazky[otazka].append(odpoved)
            print(otazky)
    return otazky # už s odpověďmi

def vyber_odpovedi(otazky_s_odpovedmi):
    for otazka in otazky_s_odpovedmi:
        if len(otazky_s_odpovedmi[otazka]) > 1:
            otazky_s_odpovedmi[otazka] = choice(otazky_s_odpovedmi[otazka])
        else:
            otazky_s_odpovedmi[otazka] = otazky_s_odpovedmi[otazka][0]
    return otazky_s_odpovedmi

def vypis_vysledek(vybrane_odpovedi):
    print(f"""
    Takže co jsme zjistili: {vybrane_odpovedi["Kdo?"]} šel s {vybrane_odpovedi["S kým?"]}
    do {vybrane_odpovedi["Kde?"]} a dělali tam {vybrane_odpovedi["Co dělali?"]}.
    To celé se stalo {vybrane_odpovedi["Kdy?"]}, ale hlavně už víme i proč: {vybrane_odpovedi["Proč?"]}
    """)   

vsechny_odpovedi = ziskej_odpovedi()
vybrane_odpovedi = vyber_odpovedi(vsechny_odpovedi)
vypis_vysledek(vybrane_odpovedi)