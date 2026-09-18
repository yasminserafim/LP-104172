import os
os.system("cls")

# ENTRADA
usuario_campo = str(input("Digite seu login: "))
senha_campo = str(input("Digite sua senha: "))
usuario = "yasmin"
senha = 12345

# PROCESSAMENTO
usuario_esta_correto = usuario_campo == usuario
senha_esta_correta = senha_campo == senha

# EXIBINDO DADOS
if usuario_esta_correto and senha_esta_correta:
    print("Bem-vindo")
else:
    print("Login ou senha inválidos")
