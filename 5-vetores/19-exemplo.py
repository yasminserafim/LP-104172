
lista_jogador = []


while True:
    os.system("cls")
    print('''
    === EC DENDEZEIROS ===
        1 - CADASTRAR JOGADORES
        2 - LISTAR TODOS OS JOGADORES
        3 - ATUALIZAR JOGADOR
        4 - REMOVER JOGADOR
        0 - SAIR
    ''')

    opcao = int(input("Escolha uma opção: "))

    match opcao:
        case 1:
            print("== CADASTRAR JOGADOR ==")
            nome_jogador = input('Digite o nome do jogador: ').strip().upper()
            posicao_jogador = input('Digite a posição do jogador: ')
            numero_jogador = int(input('Digite o número do jogador: '))
            if nome_jogador in lista_jogador:
                print("Produto já cadastrado.")
            else:
                lista_jogador.append(nome_jogador)
                print("Produto cadastrado com sucesso!")