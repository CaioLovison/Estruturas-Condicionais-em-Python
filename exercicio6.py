# Classificação de temperatura

temp = float(input("Digite a temperatura em °C: "))

if temp < 18:
    print("Frio")
elif temp <= 28:
    print("Agradável")
else:
    print("Quente")