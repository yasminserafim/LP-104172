import os
os.system("cls")


# import os os.system("cls")
# input adiciona oque for digitado no terminal na variavel como texto
# int () converte o que foi digitado em inteiro 
# float () converte o que foi digitado em reais
# \n pular linha



#solicitando dados
print("= SOLICITANDO DADOS =")
nome = input("Digite seu nome: ")
idade = int(input("Digite sua idade: "))
nota_1 = float(input("Digite sua primeira nota: "))
nota_2 = float(input("Digite sua segunda nota: "))

media = (nota_1 + nota_2) / 2

print("\n= EXIBINDO DADOS =")
print("Nome: ", nome)
print("Idade: ", idade)
print("Primeira Nota: ", nota_1)
print("Segunda Nota: ", nota_2)
print("Média: ", media)





