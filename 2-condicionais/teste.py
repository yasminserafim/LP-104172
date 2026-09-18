import os
os.system("cls")

#ENTRADA
usuario_campo = str(input("Digite seu usuário: "))
senha_campo = int(input("Digite sua senha: "))
usuario = str ("yasmin")
senha = int(12345)

#PROCESSAMENTO
if usuario_campo and senha_campo != usuario and senha:
    print("Usuário ou Senha Incorreto")
else:
    print("Bem Vindo")

