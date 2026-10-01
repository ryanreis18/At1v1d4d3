distancia = float(input("Distância: "))
Tempo = int(input("Tempo: "))
Velocidade = distancia / Tempo

if Velocidade >= 40:
    print (Velocidade, "KM/h, Modo turbo ativo.")
else: 
    print (Velocidade, "KM/h, Modo normal.")