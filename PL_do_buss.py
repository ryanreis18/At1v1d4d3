duracao_viagem = int(input("Duração da viagem: "))
duracao_musica = int(input("Duração média de uma música: "))

musgas = duracao_viagem // duracao_musica

print("Cabem", musgas, "músicas inteiras no seu anusbus.")