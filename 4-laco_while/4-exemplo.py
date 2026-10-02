import os
os.system("cls")

soma = 0
quantidade_notas = 2


for i in range (quantidade_notas):
    while True:
        nota = float(input(f"Digite sua {i+1} nota: "))
        if nota < 0 and nota > 10:
            print("Nota inválida. \nTente novamente! \n")
            input("Pressione a tecla pra continuar. . .")
            os.system("cls")
        else:
            soma += nota
            break

media = soma / quantidade_notas
print(f"Média: {media}")