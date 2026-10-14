import os
os.system("cls")

vetor_notas = []

for i in range (3):
    nota = float(input("Digite sua nota: "))
    vetor_notas.append(nota)
    
print(" = EXIBINDO NOTAS = ")
for indice, nota in enumerate (vetor_notas, start=1):
    print(f'{indice}º: {nota}')