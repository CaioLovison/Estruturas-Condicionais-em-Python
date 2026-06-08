# Calculadora simples

n1 = float(input("Primeiro número: "))
n2 = float(input("Segundo número: "))

operacao = input("Digite (+,-,*,/): ")

if operacao == "+":
    print(n1 + n2)
elif operacao == "-":
    print(n1 - n2)
elif operacao == "*":
    print(n1 * n2)
elif operacao == "/":
    if n2 != 0:
        print(n1 / n2)
    else:
        print("Divisão por zero não permitida")
else:
    print("Operação inválida")