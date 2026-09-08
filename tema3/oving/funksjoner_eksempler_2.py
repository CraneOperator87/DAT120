"""Funksjoner med if-setninger og løkker."""


def er_positivt(tall):
    """Returnerer True hvis tallet er storre enn null."""
    if tall > 0:
        return True
    else:
        return False


def storst(tall1, tall2):
    """Returnerer det storste av to tall."""
    if tall1 > tall2:
        return tall1
    else:
        return tall2


def skriv_ut_ganger(tall, antall):
    """Skriver ut tall ganger fra 1 til antall."""
    for gang in range(1, antall + 1):
        print(tall * gang)


print("Er 8 positiv?", er_positivt(8))
print("Det storste tallet er", storst(12, 9))
print("De fem forste multiplene av 3 er:")
skriv_ut_ganger(3, 5)
