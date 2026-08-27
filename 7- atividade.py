import os
os.system("cls")

#entrada
numero1 = float(input("Digite um número: "))
numero2 = float(input("Outro um número: "))

#processamento
media = (numero1 + numero2) / 2
soma = numero1 + numero2
produto = numero1 * numero2
if numero1 > numero2:
    maior = numero1
    menor = numero2
else:
    maior = numero2
    menor = numero1

#SAÍDA
print("Média: ", media)
print("Soma: ", soma)
print("Produto: ", produto)
print("Maior número: ", maior)
print("Menor número: ", menor)
