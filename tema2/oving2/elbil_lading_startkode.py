rekkevidde_km_str = input("Rekkevidden til din elbil i kilometer: ")
tur_lengde_km_str = input("Lengden til kjøreturen din i kilometer: ")
rekkevidde_km = int(rekkevidde_km_str)
tur_lengde_km = int(tur_lengde_km_str)
antall_ladinger = tur_lengde_km // rekkevidde_km
print(f"Du trenger {antall_ladinger} ladinger")
