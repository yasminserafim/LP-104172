import os
os.system("cls")

soma = 0
contador = 0

while True:
    numero = int(input("Digite um número: "))
    contador += 1
    soma += numero
    media = soma / contador
    print("Média: ", media)
    if media < 0:
        break