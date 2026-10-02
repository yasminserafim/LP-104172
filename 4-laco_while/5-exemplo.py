import os
os.system("cls")

print("= = = CADASTRO = = =")

usuario = input("Crie e digite seu usuário: ")
senha = int(input("Crie e digite sua senha: "))
os.system("cls")

print ("= = = LOGIN = = =")
campo_usuario = input("Digite seu usuário: ")
campo_senha = int(input("Digite seu usuário: "))

while True:
    if campo_usuario == usuario and campo_senha == senha:
        print ("Bem-Vindo!")
        break
    else:
        print("Usuário e senha inválidos. \n Tente novamente")
        input("Pressione Enter para continuar ...")
        os.system("cls")
        print ("= = = LOGIN = = =")
        campo_usuario = input("Digite seu usuário: ")
        campo_senha = int(input("Digite seu usuário: "))