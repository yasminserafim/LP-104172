import os
os.system("cls")

vetor_numero = []
par = 0
impar = 0

for i in range(6):
    numero = int(input("Digite um número: "))
    vetor_numero.append(numero)
    if numero % 2 == 0:
        par += 1
    else:
        impar += 1
    
print(" = EXIBINDO RESULTADOS = ")
for valor in vetor_numero:
    print("Número: ", valor)
print("Quantidade de números pares: ", par)
print("Quantidade de números impares: ", impar)