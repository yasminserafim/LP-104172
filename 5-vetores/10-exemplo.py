import os
os.system("cls")

vetor_numero = []

for i in range(5):
    numero = int(input("Digite um número: "))
    vetor_numero.append(numero)
    
maior_numero = max(vetor_numero)
menor_numero = min(vetor_numero)

print(" = EXIBINDO RESULTADOS = ")
for valor in vetor_numero:
    print("Número: ", valor)
print("Maior número: ", maior_numero)
print("Menor número: ",menor_numero)