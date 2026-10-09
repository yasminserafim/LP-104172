import os
os.system("cls")

vetor_nomes = []

for i in range(3):
    nome = str(input("Digite os nomes: "))
    vetor_nomes.append(nome) 

for i in range(3):
    print("Nomes: ", vetor_nomes)