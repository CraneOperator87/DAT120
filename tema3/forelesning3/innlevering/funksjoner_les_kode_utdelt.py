def skriv_inn_pris():
    pris = input("Pris: ")

    if pris == "":
        return None

    try:
        return float(pris)
    except ValueError:
        print("Feilformatert pris")
        return None


def skriv_inn_vartype(pris, sum_mat, sum_drikke, sum_annet):
    type_vare = input("Mat (m), drikke (d) eller annet (a): ").lower()

    if type_vare == "m":
        sum_mat += pris
        print(f"Det ble lagt til til sum mat: [{sum_mat}]")
    elif type_vare == "d":
        sum_drikke += pris
        print(f"Det ble lagt til til sum mat: [{sum_drikke}]")
    elif type_vare == "a":
        sum_annet += pris
        print(f"Det ble lagt til til sum annet: [{sum_annet}]")
    else:
        print("Ugyldig varetype")

    return sum_mat, sum_drikke, sum_annet


sum_mat = 0
sum_drikke = 0
sum_annet = 0

print("Skriv inn priser på varer og type vare.")
print("Avslutt med negativ pris eller tom input.")

while True:
    pris = skriv_inn_pris()

    if pris is None:
        break

    if pris < 0:
        break

    sum_mat, sum_drikke, sum_annet = skriv_inn_vartype(pris,sum_mat,sum_drikke,sum_annet)

print("Sum mat:", sum_mat)
print("Sum drikke:", sum_drikke)
print("Sum annet:", sum_annet)