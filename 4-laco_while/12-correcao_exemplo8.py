import os
os.system("cls")

soma = 0
quantidade_numeros = 0


while True:
    os.system("cls")
    numero = int(input("Digite um númmero: "))

    if numero >= 0:
        soma += numero
        quantidade_numeros += 1
    else:
        break

if quantidade_numeros == 0:
    print("Não foram inseridos números.")
else:
    media = soma / quantidade_numeros
    print("Média: ", media)