"""Enkle eksempler med funksjoner."""


def hils(navn):
    """Skriver ut en hilsen."""
    print(f"Hei, {navn}!")


def legg_sammen(tall1, tall2):
    """Returnerer summen av to tall."""
    sum = tall1 + tall2
    return sum


def dobbel(tall):
    """Returnerer tallet ganget med to."""
    return tall * 2


# En funksjon blir ikke kjort for vi kaller pa den.
hils("Ada")

resultat = legg_sammen(4, 7)
print("Summen er", resultat)

print("Det dobbelte av 6 er", dobbel(6))
