fil = open("tema4/obligatorisk/bronntrykk.txt", "r", encoding="utf-8")

ignorerteLinjer = 0

for linje in fil:
    linje = linje.strip() # 1.3 : Hver linje fjernes \n 

    if linje == "": # 1.4: Hoppe over tomme linjer
        ignorerteLinjer +=1; continue
    if linje.startswith("#"): # 1.5: Hoppe over kommentarer
        ignorerteLinjer +=1; continue

    print(linje)

fil.close()

print(f"\nAntall ignorerte linjer: {ignorerteLinjer}")