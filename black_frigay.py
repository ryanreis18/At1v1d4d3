compras = float(input("Valor das Comprittas: "))

if compras > 100: 
     desconto = compras * 0.15
     V_Final = compras - desconto
     print("Desconto aplicado: R$", desconto)
     print("Valor final: R$", V_Final)
else: 
     print("Nenhum desconto foi aplicado.")
     print("Valor final: R$", compras)