import os
os.system("cls")

par = 0
impar = 0
contador = 0
soma = 0

while True:
    numero = int(input("Digite um número: "))
    contador += 1
    soma += numero
    media_geral = soma / contador
    print("Média geral: ", media_geral)
    if numero % 2 == 0:
        par += 1
        print("Quantidade de pares: ", par)
        media_pares = numero / par
        print("Média de pares: ", media_pares)
    else:
        impar += 1
        print("Quantidade de ímpares: ", impar)
    if media_geral < 0:
        break


