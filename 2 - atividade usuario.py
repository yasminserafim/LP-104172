import os
os.system("cls")

# ENTRADA
usuario_campo = str(input("Digite seu login: "))
senha_campo = str(input("Digite sua senha: "))
usuario = "yasmin"
senha = 12345

# EXIBINDO DADOS
if usuario == usuario_campo and senha == senha_campo:
    print("Bem-Vindo!")
else:
    print("Login ou senha inválidos")