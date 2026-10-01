bateria = float (input("Digite a carga atual da bateria: "))
consumo = float (input("Digite o quanto ele consome por hora: "))

hora = bateria / consumo
print(f"A bateria ainda vai durar {hora} horas")
if bateria < 20:
    print("A bateria ta fraca, corre pra tomada!")
if not bateria < 20:
    print("A bateria ta boa, não precisa carregar o celular")