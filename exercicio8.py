# Cálculo de aumento salarial

salario = float(input("Digite o salário: "))

if salario <= 2000:
    aumento = salario * 0.10
else:
    aumento = salario * 0.05

novo_salario = salario + aumento

print("Novo salário:", novo_salario)