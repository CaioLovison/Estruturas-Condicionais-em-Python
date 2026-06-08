# Login com usuário e senha

usuario = input("Usuário: ")
senha = input("Senha: ")

if usuario == "admin" and senha == "123":
    print("Login realizado")
else:
    print("Login inválido")