import os
os.system("cls")

nota = float(input("Digite uma nota de 0 a 10: "))

while True:
    if nota < 0 or nota > 10:
        print("Nota inválida")
        print("Tente novamente")
    else:
        print("Nota: ", nota)
        break