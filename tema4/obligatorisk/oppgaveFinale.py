# Leser inputfilen og logger feil
with open("tema4/obligatorisk/bronntrykk.txt", "r", encoding="utf-8") as input_fil:
    linjer = input_fil.readlines()

logg_tekster = []
ignorerte_linjer = 0
feil_antall = 0
gyldige_antall = 0
total = 0
min_verdi = None
max_verdi = None

for linje_nr, linje in enumerate(linjer, start=1):
    linje = linje.strip()

    # 1. Ignorer tom linjer
    if linje == "":
        logg_tekster.append(f"Linje {linje_nr}: {linje} - tom linje\n")
        ignorerte_linjer += 1; continue
    # 2. Ingorerer kommentarlinjer
    if linje.startswith("#"):
        logg_tekster.append(f"Linje {linje_nr}: {linje} - kommentar\n")
        ignorerte_linjer += 1; continue
    
    deler = linje.split()

    # 3. Ingen enhet: antas å være bar, men logges som advarsel
    if len(deler) == 1:
        try:
            verdi = float(deler[0].replace(",", "."))
            verdi_bar = verdi
            logg_tekster.append(f"Linje {linje_nr}: {linje} - ingen enhet, antatt bar\n")
        except ValueError:
            logg_tekster.append(f"Linje {linje_nr}: {linje} - ugyldig tall\n")
            feil_antall += 1; continue

    # 4. Tall + enhet
    elif len(deler) == 2:
        talltekst = deler[0]
        enhet = deler[1]

        try:
            verdi = float(talltekst.replace(",", "."))
        except ValueError:
            logg_tekster.append(f"Linje {linje_nr}: {linje} - ugyldig tall\n")
            feil_antall += 1; continue

        if enhet.lower() == "bar":
            verdi_bar = verdi

        elif enhet == "MPa":
            verdi_bar = verdi * 10

        elif enhet == "mPa":
            logg_tekster.append(f"Linje {linje_nr}: {linje} - ikke støttet enhet\n")
            feil_antall += 1; continue

        else:
            logg_tekster.append(f"Linje {linje_nr}: {linje} - ukjent enhet\n")
            feil_antall += 1; continue

    else:
        logg_tekster.append(f"Linje {linje_nr}: {linje} - feil format\n")
        feil_antall += 1; continue

    # 5. Oppdater statistikk for gyldige verdier
    gyldige_antall += 1
    total += verdi_bar

    if min_verdi is None or verdi_bar < min_verdi:
        min_verdi = verdi_bar

    if max_verdi is None or verdi_bar > max_verdi:
        max_verdi = verdi_bar

# 6. Gjennomsnitt
if gyldige_antall > 0:
    gjennomsnitt = total / gyldige_antall
else:
    gjennomsnitt = 0

# 7. Skriv rapport.txt
with open("tema4/obligatorisk/rapport.txt", "w", encoding="utf-8") as rapport_fil:
    rapport_fil.write(f"Antall gyldige målinger: {gyldige_antall}\n")
    rapport_fil.write(f"Sum: {total}\n")
    rapport_fil.write(f"Minimum: {min_verdi if min_verdi is not None else 0}\n")
    rapport_fil.write(f"Maksimum: {max_verdi if max_verdi is not None else 0}\n")
    rapport_fil.write(f"Gjennomsnitt: {gjennomsnitt:.2f}\n")

# 8. Skriv logg.txt
with open("tema4/obligatorisk/logg.txt", "w", encoding="utf-8") as logg_fil:
    for tekst in logg_tekster:
        logg_fil.write(tekst)

    logg_fil.write(f"\nAntall gyldige målinger: {gyldige_antall}\n")
    logg_fil.write(f"Antall linjer ignorert: {ignorerte_linjer}\n")
    logg_fil.write(f"Antall linjer med feil: {feil_antall}\n")
    logg_fil.write(f"Minimum: {min_verdi if min_verdi is not None else 0}\n")
    logg_fil.write(f"Maksimum: {max_verdi if max_verdi is not None else 0}\n")
    logg_fil.write(f"Gjennomsnitt: {gjennomsnitt:.2f}\n")

print("Programmet er ferdig.")
print(f"Gyldige målinger: {gyldige_antall}")
print(f"Feil: {feil_antall}")
print(f"Ignorerte linjer: {ignorerte_linjer}")
print(f"Minimum: {min_verdi if min_verdi is not None else 0}")
print(f"Maksimum: {max_verdi if max_verdi is not None else 0}")
print(f"Gjennomsnitt: {gjennomsnitt:.2f}")