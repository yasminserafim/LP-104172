import os
os.system("cls")

soma = 0
quantidade_nota = 0

while True:
    os.system("cls")
    print('''
    = = = MENU = = =
    S - Inserir uma nota
    N - Calcular média aritmética
    ''')

    resposta = input("Deseja inserir alguma nota? ")

    match resposta:
        case "S":
            nota = float(input("Digite uma nota: "))
            soma += nota
            quantidade_nota += 1
        case "N":
            break
        case _:
            print("Inválido")
            input("Pressione uma tecla para continuar...")

if quantidade_nota == 0:
    print("Não foram inseridas notas.")
else: 
    media = soma / quantidade_nota
    print("Média: ", media)



