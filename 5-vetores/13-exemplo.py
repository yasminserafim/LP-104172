import os
os.system("cls")

vetor_numero = []

for i in range(5):
    numero = int(input("Digite um número: "))
    if numero > 0:
        vetor_numero.append(numero)
    else:
        numero_negativo = 0
        vetor_numero.append(numero_negativo)

print("= EXIBINDO NÚMEROS DO VETOR =")
for valor in vetor_numero:
    print("Números: ", valor)