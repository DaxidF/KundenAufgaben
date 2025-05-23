integer_werte = [1, 2, 3, 2, 4]
string_werte = ["Apfel", "Banane", "Apfel", "Kirsche", "Mango"]
boolean_werte = [True, False, True, True, False]

print("Ursprüngliche Listen:")
print("Integer:", integer_werte)
print("Strings:", string_werte)
print("Booleans:", boolean_werte)

integer_werte.remove(1)
string_werte.remove("Kirsche")
boolean_werte.remove(False)

print("\nNach Entfernen eines Elements, das nur einmal vorkommt:")
print("Integer:", integer_werte)
print("Strings:", string_werte)
print("Booleans:", boolean_werte)

boolean_werte.remove(True)
string_werte.remove("Apfel")
integer_werte.remove(2)

wert_int = 2
wert_str = "Apfel"
wert_bool = True

integer_werte = [i for i in integer_werte if i != wert_int]
string_werte = [s for s in string_werte if s != wert_str]
boolean_werte = [b for b in boolean_werte if b != wert_bool]

print("\nNach Entfernen aller Vorkommen eines bestimmten Werts:")
print("Integer:", integer_werte)
print("Strings:", string_werte)
print("Booleans:", boolean_werte)