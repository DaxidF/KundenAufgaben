s = 0
i = 0
while True:
    i = int(input("Gib Zahl ein"))
    if i < 0:
        exit() #oder break
    s = s + i
    print(s)

