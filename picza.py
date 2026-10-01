fatias = int(input("Quantas fatias tem a pizza? "))
amigos = int(input("Quantos amigos estão na mesa? "))

por_pessoa = fatias // amigos
sobras = fatias % amigos

print("Cada amigo vai comer", por_pessoa, "fatias.")

if sobras > 0:
    print("Vai sobrar", sobras, "fatia(s).")
else:
    print("Não vai sobrar nenhuma fatia.")