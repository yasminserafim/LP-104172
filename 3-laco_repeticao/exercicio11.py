import os
os.system("cls")

par = 0
impar = 0
soma = 0

for i in range(5):
    numero = int(input("Digite um número inteiro: "))
    if numero % 2 == 0:
        par += 1
    else:
        impar += 1

print("Quantidade de pares: ", par)
print("Quantidade de impares: ", impar)
