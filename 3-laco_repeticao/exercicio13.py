import os
os.system("cls")

nota = 0

for i in range(3):
    nota += float(input("Digite suas notas: "))
    media = nota / 3
    if media >= 7:
        resultado = "Aprovado"
    elif media >= 4:
        resultado = "Recuperação"
    else:
        resultado = "Reprovado"


print("Sua média é: ", media)
print("Situação; ", resultado)