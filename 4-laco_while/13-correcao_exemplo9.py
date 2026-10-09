import os
os.system("cls")


soma_pares = 0
soma_geral = 0
quantidade_numeros = 0
quantidade_pares = 0
quantidade_impares = 0
quantidade_geral = 0


while True:
    os.system("cls")
    numero = int(input("Digite um número: "))

    if numero >= 0:
        quantidade_numeros += 1
        soma_geral += numero

        if numero % 2 == 0:
            quantidade_pares += 1
            soma_geral += numero
        else: quantidade_impares += 1
    else:
        break

if quantidade_geral == 0:
    print("Não foram inseridos números.")
else:
    media_geral = soma_geral / quantidade_geral
    media_pares = soma_pares / quantidade_pares

print("Média geral: ", media_geral)
print("Média pares: ", media_pares)