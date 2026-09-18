import os
os.system("cls")

#ENTRADA
numero1 = int(input("Digite um número: "))
numero2 = int(input("Digite outro número: "))

#PROCESSAMENTO
media = (numero1 + numero2) / 2
soma = numero1 + numero2
multiplicacao = numero1 * numero2
maior = max(numero1, numero2)
menor = min(numero1, numero2)

#SAÍDA
print(" = EXIBINDO RESULTADOS = ")
if numero1 == numero2:
    print("Os números são iguais")
print("Média: ", media)
print("Soma: ", soma)
print("Multiplicação: ", multiplicacao )
print("Maior: ", maior)
print("Menor: ", menor)
