import os
os.system("cls")

# ENTRADA 
media = float(input("Digite sua média: "))
falta = int(input("Digite seu numero de faltas: "))

# PROCESSAMENTO
if media >= 7.0 and falta <= 40:
    print("Aprovada(o)")
else:
    print("Reprovado")
