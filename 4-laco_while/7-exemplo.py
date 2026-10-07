import os
os.system("cls")

contador = 0

while True:
    primeira_nota = float(input("Digite sua nota: "))
    outra_nota = str(input("Se deseja inserir mais uma nota pressione N: "))
    contador += 1
    if outra_nota != "N":
        break
    elif contador > 2:
        break
    else:
        segunda_nota = float(input("Digite sua outra nota: "))
        media = primeira_nota + segunda_nota / 2
        print("Sua média é: ", media)
        break
