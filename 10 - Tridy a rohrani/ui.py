"""Grafické rozhraní pro hru Šachy.

Používá knihovnu Pyglet; pro úvod do grafiky viz:
    https://naucse.python.cz/course/pyladies/intro/pyglet/
"""

import pyglet

from sachy import Sachovnice


okno = pyglet.window.Window(width=360, height=360, resizable=True)
sachovnice = Sachovnice()
pozice_mysi = [0, 0]

obrazky = {}

def kresli_obrazek(jmeno, radek, sloupec):
    """Nakreslí obrázek na danou pozici"""

    # Načtené obrázky ukládáme ve slovníku "obrazky",
    # aby se nemusely načítat víckrát
    try:
        obrazek = obrazky[jmeno]
    except KeyError:
        # Když ještě obrázek ve slovníku není, načíst a uložit
        obrazek = pyglet.image.load(f"{jmeno}.png")
        obrazky[jmeno] = obrazek

    # Vykreslení obrázku
    velikost = min(okno.width, okno.height) / 8
    obrazek.blit(
        sloupec * velikost, radek * velikost,
        width=velikost, height=velikost,
    )

@okno.event
def on_draw():
    """Vykreslí obsah okna"""

    okno.clear()
    # Lepší vykreslování (pro nás zatím kouzelné zaříkadlo)
    pyglet.gl.glEnable(pyglet.gl.GL_BLEND)
    pyglet.gl.glBlendFunc(
        pyglet.gl.GL_SRC_ALPHA,
        pyglet.gl.GL_ONE_MINUS_SRC_ALPHA,
    )

    sachovnice.vykresli_se(kresli_obrazek)

    # Vykreslení "stínu" figurky, která se hýbe
    radek, sloupec = pozice_mysi
    figurka = sachovnice.vrat_vybranou_figurku()
    if figurka:
        pyglet.gl.glColor4f(1, 1, 1, 0.5)
        kresli_obrazek(f'{figurka.strana}_{figurka.druh}', radek, sloupec)
        pyglet.gl.glColor4f(1, 1, 1, 1)
        if sachovnice.muze_tahnout(pozice_mysi):
            kresli_obrazek('muze', radek, sloupec)
        else:
            kresli_obrazek('nemuze', radek, sloupec)


def pozice_na_souradnicich(x, y):
    """Vrátí pozici (radek, sloupec) na pixelových souřadnicích (x, y)"""
    velikost = min(okno.width, okno.height) / 8
    sloupec = int(x / velikost)
    radek = int(y / velikost)
    return radek, sloupec

@okno.event
def on_mouse_press(x, y, tlacitko, mod):
    """Zpracuje zmáčknutí tlačítka myši"""
    pozice = pozice_na_souradnicich(x, y)
    sachovnice.vyber_pozici(pozice)
    pozice_mysi[:] = pozice_na_souradnicich(x, y)

@okno.event
def on_mouse_release(x, y, tlacitko, mod):
    """Zpracuje puštění tlačítka myši"""
    pozice = pozice_na_souradnicich(x, y)
    sachovnice.tahni_na_pozici(pozice)

@okno.event
def on_mouse_drag(x, y, dx, dy, tlacitko, mod):
    """Zpracuje tažení myší"""
    pozice_mysi[:] = pozice_na_souradnicich(x, y)


pyglet.app.run()
