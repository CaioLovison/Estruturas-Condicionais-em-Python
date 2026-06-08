# Cálculo de energia elétrica

tipo = input("Tipo (R para Residencial / C para Comercial): ").upper()
consumo = float(input("Consumo em kWh: "))

if tipo == "R":
    valor = consumo * 0.60
elif tipo == "C":
    valor = consumo * 0.75
else:
    valor = 0
    print("Tipo inválido")

print("Valor a pagar: R$", valor)