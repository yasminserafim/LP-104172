import os
os.system("cls")

vetor_nota = []

for i in range(3):
    nota = float(input("Digite sua nota: "))
    vetor_nota.append(nota)
    
soma = sum(vetor_nota)
media = soma / 3

print(" = EXIBINDO NOTAS = ")
for indice, nota in enumerate (vetor_nota, start=1):
    print(f'{indice}º: {nota}')

print("Média: ",media)