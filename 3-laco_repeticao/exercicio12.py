import os
os.system("cls")

nota = 0

for i in range(4):
    nota += float(input("Digite suas notas: "))
    media = nota / 4


print("Sua soma de notas é: ", nota)
print("Sua média é: ", media)