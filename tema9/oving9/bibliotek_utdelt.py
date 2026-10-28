class Bok:
    def __init__(self, tittel, forfatter, utgivelsesaar, antall_totalt=1):
        self.tittel = tittel
        self.forfatter = forfatter
        self.utgivelsesaar = utgivelsesaar
        self.antall_totalt = antall_totalt
        self.antall_naa = antall_totalt

    def __str__(self):
        ledig = self.antall_naa > 0
        status = "ledig" if ledig else "ikke ledig"
        return f"{self.tittel} av {self.forfatter} ({self.utgivelsesaar}) - {status}"

    def laan_ut(self):
        if self.antall_naa == 0:
            return False
        self.antall_naa -= 1
        return True

    def lever_inn(self):
        self.antall_naa += 1


class Bibliotek:
    def __init__(self, boker=None):
        self.boker = [] if boker is None else boker

    def legg_til_bok(self, bok):
        self.boker.append(bok)

    def vis_alle_boker(self):
        if not self.boker:
            print("Biblioteket har ingen bøker.")
            return

        for nummer, bok in enumerate(self.boker, start=1):
            print(f"{nummer}. {bok}")


def _les_heltall(prompt, minimum=None):
    while True:
        try:
            verdi = int(input(prompt))
        except ValueError:
            print("Skriv inn et heltall.")
            continue

        if minimum is not None and verdi < minimum:
            print(f"Tallet må være minst {minimum}.")
            continue
        return verdi


def _velg_bok(bibliotek):
    if not bibliotek.boker:
        print("Biblioteket har ingen bøker.")
        return None

    bibliotek.vis_alle_boker()
    nummer = _les_heltall("Velg boknummer: ", 1)
    if nummer > len(bibliotek.boker):
        print("Ugyldig boknummer.")
        return None
    return bibliotek.boker[nummer - 1]


def legg_til_bok_fra_input(bibliotek):
    tittel = input("Tittel: ").strip()
    forfatter = input("Forfatter: ").strip()
    utgivelsesaar = _les_heltall("Utgivelsesår: ")
    antall = _les_heltall("Antall eksemplarer totalt: ", 1)
    bibliotek.legg_til_bok(Bok(tittel, forfatter, utgivelsesaar, antall))
    print("Boka ble lagt til.")


def start_avstandskonvertering():
    antall = float(input("Antall: "))
    fra_enhet = input("Fra enhet: ")
    til_enhet = input("Til enhet: ")
    resultat = konverter_avstand(antall, fra_enhet, til_enhet)
    print(f"{antall:g} {fra_enhet} = {resultat:g} {til_enhet}")


def start_bibliotek():
    bibliotek = Bibliotek()

    while True:
        print("\n1. Legg til bok")
        print("2. Lån ut bok")
        print("3. Lever inn bok")
        print("4. Vis alle bøker")
        print("5. Avslutt")
        valg = input("Velg: ").strip()

        if valg == "1":
            legg_til_bok_fra_input(bibliotek)
        elif valg == "2":
            bok = _velg_bok(bibliotek)
            if bok is not None:
                if bok.laan_ut():
                    print("Utlånet ble registrert.")
                else:
                    print("Utlån mislyktes: Ingen eksemplarer er ledige.")
        elif valg == "3":
            bok = _velg_bok(bibliotek)
            if bok is not None:
                bok.lever_inn()
                print("Innleveringen ble registrert.")
        elif valg == "4":
            bibliotek.vis_alle_boker()
        elif valg == "5":
            break
        else:
            print("Ugyldig valg.")


if __name__ == "__main__":
    print("Avstandskonvertering")
    start_avstandskonvertering()
    print("\nBibliotek")
    start_bibliotek()
