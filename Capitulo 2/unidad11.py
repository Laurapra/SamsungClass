capital_dic = {"Corea": "Seúl", "Alemania": "Berlín",
               "Francia": "París", "Italia": "Roma", "España": "Madrid"}
print(capital_dic["Corea"])

# quiz02:
frutas_dic = {"manzana": 0.5, "banana": 0.25,
              "pera": 0.75, "naranja": 0.3, "uva": 1.0}
for fruta, precio in frutas_dic.items():
    print("El precio de la", fruta, "es", precio, "dólares.")

# quiz03:
frutas_dic = {"manzana": 6000, "melón": 3000, "banano": 5000, "naranja": 4000}
claves = list(frutas_dic.keys())
print("claves_diccionario", claves)

if "manzana" in frutas_dic:
    print("manzana is in frutas_dic.")
else:
    print("manzana is not in frutas_dic.")

if "mango" in frutas_dic:
    print("mango is in frutas_dic.")
else:
    print("mango is not in frutas_dic.")
