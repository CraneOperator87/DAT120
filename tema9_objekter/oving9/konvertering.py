avstandsenheter = {
    "centimeter": 0.01,
    "tomme": 0.0254,
    "fot": 0.3048,
    "yard": 0.9144,
    "meter": 1,
    "kilometer": 1000,
    "miles": 1609,
    "nautisk mil": 1852,
    "mil": 10000,
}


def konverter_avstand(antall, fra_enhet, til_enhet):
    """Konverterer en avstand mellom to enheter."""
    fra_enhet = fra_enhet.strip().lower()
    til_enhet = til_enhet.strip().lower()

    #Sjekk om enheten er i bibloteket
    if fra_enhet not in avstandsenheter: raise ValueError(f"Ukjent enhet: {fra_enhet}")
    if til_enhet not in avstandsenheter: raise ValueError(f"Ukjent enhet: {til_enhet}")

    # Fra enhet -> Meter -> Til enhet
    antall_meter = antall * avstandsenheter[fra_enhet]
    return antall_meter / avstandsenheter[til_enhet]


def les_antall():
    """Leser et tall fra brukeren og godtar både punktum og komma."""
    while True:
        tekst = input("Skriv inn antall: ").strip().replace(",", ".")
        try:
            return float(tekst)
        except ValueError: print("Du må skrive inn et tall.")


def main():
    antall = les_antall()
    fra_enhet = input("Fra hvilken måleenhet? ").strip().lower()
    til_enhet = input("Til hvilken måleenhet? ").strip().lower()

    try:
        resultat = konverter_avstand(antall, fra_enhet, til_enhet)
    except ValueError as feil: print(feil); return

    print(f"{antall} {fra_enhet} = {resultat} {til_enhet}")



if __name__ == "__main__": main()