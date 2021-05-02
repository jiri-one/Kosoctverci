text_pisne = """
Raketou na Mars
poletíme zas - ty a já.
Raketou jen já a ty
a to touhletou - jen pro nás.Raketou na Mars
poletíme zas,
no tak pěkný počasí, to se ví, chtěj mít.
Doufej, že vesmír neznámý uvidí, kdo jsme my - já a tyRaketou na Mars
poletíme zas - já a ty.
Raketou jen já a ty,
všechny hvězdy jsou jen pro nás.
Raketou na Mars
sobě pro radost,
a jak láska ve mně plá a plá a plápolá,
tou rourou z ocele letíme, přátele, ke hvězdám.Vooooo...Kdo tu sílu má,
milovat jak já
a ta láska ve mně plá a plá a plápolá
láska nás povznáší, láska nás vynáší ke hvězdám.Vooooo...Raketou na Mars
vooooo...
"""

pocet_pismen = 0

for znak in text_pisne:
    if znak in " \n!\"#$%&\'()*+,-./:;<=>?@[\]^_{|}~":
        pass
    else:
        pocet_pismen += 1

print("Počet písmen v písničce je: ", pocet_pismen)
