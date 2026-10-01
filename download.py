preco = float(input("Digite o preço do salgado (R$): "))
dinheiro = float(input("Digite o valor colocado na máquina (R$): "))

if dinheiro < preco:
    print("Saldo insuficiente, passa fome.")
else:
    troco = dinheiro - preco
    print(f"Troco: R$ {troco:.2f}")