import os
os.system("cls")

vetor_nota = []

for i in range(4):
    nota = float(input("Digite sua nota: "))
    vetor_nota.append(nota)
    
soma = sum(vetor_nota)
media = soma / 4

print(" = EXIBINDO NOTAS = ")
for indice, nota in enumerate (vetor_nota, start=1):
    print(f '{indice}º: {nota}')
    
if media >= 7:
    resultado = "Aprovado"
elif media >= 5:
    resultado = "Recuperação"
else:
    resultado = "Reprovado"

print("Soma: ", soma)
print("Média: ",media)
print("Situação: ", resultado)