

def skriv_tall (variabel):
    manglerVerdi = True
    while manglerVerdi:
        try: 
            romLengde = float(input(variabel))
        except ValueError:
            print("Lengden må være et tall")
            continue
        if romLengde < 0.0:
            print("Lengden må være positiv")
            continue
        else:
            manglerVerdi = False
    return romLengde

lengde = skriv_tall("Hva er lengden til rommet?: ")
bredde = skriv_tall("Hva er bredden til rommet?: ")
hoyde = skriv_tall("Hva er høyden til rommet?: ")

volum = lengde * bredde * hoyde
print(f"Volumet til rommet er: {volum:.2f}")