import os
os.system("cls")

# ENTRADA
nome_aluno = str(input("Digite o seu nome: "))
nota1 = float(input("Digite sua primeira nota: "))
nota2 = float(input("Digite sua segunda nota: "))

# PROCESSAMENTO
media = nota1 + nota2 / 2

if media >= 9:
    conceito = "A"
elif media >= 7.5:
    conceito = "B"
elif media >= 6:
    conceito = "C"
elif media >= 4:
    conceito = "D"
else: conceito = "E"

if media >= 6:
    resultado = "Aprovado"
else: resultado = "Reprovado"

# SAÍDA
print("\n= RESULTADO =")
print("")