Liste = []
for x in range(0, 6):
    Liste.append(x)
print(Liste)

Liste.append("Hallo")
Liste.append("Welt")
Liste.append("Python")
print(Liste)

Liste1 = []
for x in range(0, 11):
    if (x%2) == 0:
        Liste1.append(x)
print(Liste1)

namen = []
for x in range(0, 3):
    r = input("Bitte gib den Namen ein: ")
    namen.append(r)
print(namen)