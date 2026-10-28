AVSTANDSENHETER = {
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
    """Konverterer en avstand mellom enhetene i AVSTANDSENHETER."""
    fra_enhet = fra_enhet.strip().lower()
    til_enhet = til_enhet.strip().lower()

    if fra_enhet not in AVSTANDSENHETER:
        raise ValueError(f"Ukjent enhet: {fra_enhet}")
    if til_enhet not in AVSTANDSENHETER:
        raise ValueError(f"Ukjent enhet: {til_enhet}")

    meter = antall * AVSTANDSENHETER[fra_enhet]
    return meter / AVSTANDSENHETER[til_enhet]

