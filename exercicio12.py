# Idade e votação

ano = int(input("Ano de nascimento: "))

idade = 2026 - ano

print("Idade:", idade)

if idade >= 16:
    print("Pode votar")
else:
    print("Não pode votar") 