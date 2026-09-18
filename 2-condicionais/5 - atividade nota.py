import os
os.system("cls")

# ENTRADA
nota = float(input("Digite sua nota: "))

# PROCESSAMENTO
if nota >= 0 and nota <= 10:
    print(nota)
else:
    print("A nota deve ser entre 0 e 10")