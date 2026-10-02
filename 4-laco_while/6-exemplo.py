import os
os.system("cls")

soma = 0

for i in range (3):
    while True:
        nota = float(input("Digite sua nota: "))
        if nota < 0 and nota > 10:
                    print("Nota inválida. \nTente novamente! \n")
                    input("Pressione a tecla pra continuar. . .")
                    os.system("cls")
        else:
               soma += nota
               break

media = soma / 3

if media >= 7:
    resultado = "Aprovado"
elif media >= 5:
    resultado = "Recuperação"
else:
    resultado = "Reprovado"

print(media)
print(resultado)