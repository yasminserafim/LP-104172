import os
os.system("cls")

print("= INSERINDO 5 NOME DE LIVROS =")
vetor_nome_livros = []

for i in range(5):
    livros = str(input("Digite o nome dos livros: "))
    vetor_nome_livros.append(livros)

print("= EXIBINDO NÚMEROS DO VETOR =")
for valor in vetor_nome_livros: # ForEach
    print("Nome do livro: ", valor)