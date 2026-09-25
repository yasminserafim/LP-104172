import os
os.system("cls")

soma = 0

for i in range(3):
    numero = int(input("Digite um número para somar: "))
    soma = soma + numero
    print("Valor temporario da variavel soma: ", soma)

print("Valor final da váriavel soma: ", soma)