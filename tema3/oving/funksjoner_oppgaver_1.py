"""Oppgaver: grunnleggende funksjoner.

Skriv kode under hver funksjon. Test funksjonene med kall nederst i filen.
"""


def velkomst(navn):
    """Oppgave 1: Skriv ut en hyggelig velkomst til navnet."""
    print(f"Hei og velkommen {navn}!")


def areal_rektangel(lengde, bredde):
    """Oppgave 2: Returner arealet av et rektangel."""
    return lengde * bredde


def omkrets_rektangel(lengde, bredde):
    """Oppgave 3: Returner omkretsen av et rektangel."""
    return lengde * 2 + bredde * 2


def celsius_til_fahrenheit(celsius):
    """Oppgave 4: Returner temperatur i Fahrenheit.

    Formel: fahrenheit = celsius * 9 / 5 + 32
    """
    fahrenheit = celsius * 9/5 + 32
    print(f"{celsius} Celsius -> {fahrenheit} Fahrenheit")

def fahrenheit_til_celsius(fahrenheit):
    """Returnerer temperatur fra fahrenheit til celsius."""

    celsius = (fahrenheit - 32) * (5/9)
    print(f"{fahrenheit} Fahrenheit -> {celsius} celsius ")


velkomst("Kajus")
print(f"Arealet for gitt rektangel er gitt ved: {areal_rektangel(2,5)}")
print(f"Omkretsen til en rektangel med gitt verdier: {omkrets_rektangel(2,5)}")
celsius_til_fahrenheit(20)
fahrenheit_til_celsius(68)
