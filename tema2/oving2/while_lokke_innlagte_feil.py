import random

mitt_Tall = random.randint(1, 1000)
ditt_tall = 0
antall_forsok = 0
print("Jeg har et tall mellom 1 og 1000. Du ska gjette mitt tall på færrest mulig forsøk")
while True:
    ditt_tall = int(input("Hva gjetter du? "))
    if ditt_tall < mitt_Tall:
        print("Ditt tall er mindre enn mitt tall.")
    elif ditt_tall > mitt_Tall:
        print("Ditt tall er større enn mitt tall.")
    else:
        print(f"Gratulerer! Du gjettet riktig. Du brukte {antall_forsok} forsøk.")
        antall_forsok += 1
