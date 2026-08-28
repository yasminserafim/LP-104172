import os
os.system("cls")

#ENTRADA
idade = int(input("Digite sua idade: "))

#PROCESSAMENTO
if idade < 16:
    print("Não podem votar.")
elif idade <= 17:
    print("Voto opcional")
elif idade <= 65:
    print("Voto obrigatório")
else: ("Não é obrigatório votar")
