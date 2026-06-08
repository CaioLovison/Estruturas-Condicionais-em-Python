# Maior entre três números

n1 = float(input("Primeiro número: "))
n2 = float(input("Segundo número: "))
n3 = float(input("Terceiro número: "))

if n1 >= n2 and n1 >= n3:
    print("Maior:", n1)
elif n2 >= n1 and n2 >= n3:
    print("Maior:", n2)
else:
    print("Maior:", n3)