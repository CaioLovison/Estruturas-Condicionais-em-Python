# Aprovação de empréstimo

salario = float(input("Salário: "))
parcela = float(input("Valor da parcela: "))

if parcela <= salario * 0.30:
    print("Empréstimo aprovado")
else:
    print("Empréstimo negado")