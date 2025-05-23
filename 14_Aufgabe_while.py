wort = ""
Liste = ["Haha", "Ha", "Hahahaha", "H", "Hahaha"]
leng = 0

for x in Liste:
    if leng < len(x):
        wort = x
        leng = len(x)
print(wort)
print(leng)