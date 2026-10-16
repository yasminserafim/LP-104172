import os
os.system("cls")

vetor_numero = []
contador = 0
soma = 0

for i in range(5):
    numero = float(input("Digite um número: "))
    vetor_numero.append(numero)
    if numero < 0:
        contador += 1
        print("Quantidade de números negativos: ", contador)
    else:
        soma = numero + soma
        print("Soma dos números positivos: ", soma)