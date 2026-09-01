sum_mat = 0
sum_drikke = 0
sum_annet = 0

def skriv_inn_pris():
    pris = input("Pris: ")
    if pris == "":
        return None
    try:
        pris = float(pris)
    except ValueError:
        print("Feilformatert pris")
        return None

def skriv_inn_vartype():
    type_vare = input("Mat (m) eller drikke (d) eller annet (a)")
    if type_vare[0].lower() == "m":
        sum_mat += pris
    elif type_vare[0].lower() == "d":
        sum_drikke += pris
    else:
        sum_annet += pris

fortsetter = True
print("Skriv inn priser på varer og type vare. Avslutt med negativ pris")
while fortsetter:
    skriv_inn_pris()
    if pris < 0.0:
        fortsetter = False
        break
    skriv_inn_vartype()
print("Sum mat: ", sum_mat)
print("Sum drikke: ", sum_drikke)
print("Sum annet: ", sum_annet)
