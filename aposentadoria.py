import os
os.system("cls")

# ENTRADA
codigo = int(input("Digite seu código: "))
nascimento = int(input("Digite seu ano de nascimento: "))
tempo_trabalho = float(input("Digite seu tempo de trabalho: "))

# SAÍDA
print(codigo)
print(nascimento)
print(tempo_trabalho)
if nascimento > 1961 and tempo_trabalho < 30:
    print("Não requerer aposentadoria")
else:
    print("Requerer aposentadoria")