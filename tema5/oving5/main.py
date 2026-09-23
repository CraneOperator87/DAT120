import csv
from datetime import datetime
from pathlib import Path

import matplotlib.pyplot as plt


DATAFIL = Path(__file__).with_name("timestrafikk_sykkelmotorveien_juni_2026.csv")
RETNINGER = {
	"Totalt i retning Stavanger": "Stavanger",
	"Totalt i retning Sandnes": "Sandnes",
}


def les_data():
	"""Leser trafikkdataene fra CSV-filen."""
	with DATAFIL.open(encoding="utf-8-sig", newline="") as fil:
		return list(csv.DictReader(fil, delimiter=";"))


def les_dato(data):
	"""Ber om en dato på formatet YYYY-MM-DD og sjekker at den finnes."""
	tilgjengelige_datoer = sorted({rad["Dato"] for rad in data})

	while True:
		dato = input("Skriv inn dato (YYYY-MM-DD): ").strip()

		try:
			datetime.strptime(dato, "%Y-%m-%d")
		except ValueError:
			print("Ugyldig datoformat. Bruk YYYY-MM-DD, for eksempel 2026-06-01.")
			continue

		if dato not in tilgjengelige_datoer:
			print("Datoen finnes ikke i datafilen.")
			print("Tilgjengelige datoer:", ", ".join(tilgjengelige_datoer))
			continue

		return dato


def les_passeringer(verdi):
	if not verdi or verdi.strip() == "-":
		return 0
	return int(float(verdi.replace(",", ".")))


def hent_timesdata(data, dato):
	"""Henter passeringer per time og retning for valgt dato."""
	timesdata = {retning: [0] * 24 for retning in RETNINGER.values()}

	for rad in data:
		if rad["Dato"] != dato or rad["Felt"] not in RETNINGER:
			continue

		time = int(rad["Fra tidspunkt"].split(":")[0])
		passeringer = les_passeringer(rad["Trafikkmengde"])
		retning = RETNINGER[rad["Felt"]]
		timesdata[retning][time] = passeringer

	return timesdata


def lag_plott(timesdata, dato):
	timer = range(24)
	plt.plot(timer, timesdata["Stavanger"], marker="o", label="Mot Stavanger")
	plt.plot(timer, timesdata["Sandnes"], marker="o", label="Mot Sandnes")
	plt.xticks(range(24))
	plt.xlabel("Time på døgnet")
	plt.ylabel("Antall sykkelpasseringer")
	plt.title(f"Sykkelpasseringer {dato}")
	plt.grid(True, alpha=0.3)
	plt.legend()
	plt.tight_layout()
	plt.show()


def main():
	data = les_data()
	dato = les_dato(data)
	timesdata = hent_timesdata(data, dato)
	lag_plott(timesdata, dato)


if __name__ == "__main__":
	main()
