import os

lista_produtos = []

while True:
    os.system("cls")
    print('''
    === MERCADINHO DENDEZEIROS ===
    1 - CADASTRAR PRODUTO
    2 - LISTAR TODOS OS PRODUTOS
    3 - ATUALIZAR PRODUTO
    4 - REMOVER PRODUTO
    5 - BUSCAR PRODUTO
    0 - SAIR
    ''')

    opcao = int(input("Escolha uma opção: "))

    match opcao:
        case 1:
            print("== CADASTRAR PRODUTO ==")
            nome_produto = input('Digite o nome do produto: ').strip().upper()
            if nome_produto in lista_produtos:
                print("Produto já cadastrado.")
            else:
                lista_produtos.append(nome_produto)
                print("Produto cadastrado com sucesso!")
        case 2:
            print("== PRODUTOS NO ESTOQUE ==")
            for produto in lista_produtos:
                print(f'- {produto}')
            print(f'Total: {len(lista_produtos)}')
        case 3:
            print('== ATUALIZAR PRODUTO ==')
            nome = input("Qual produto deseja atualizar? ")
            if nome in lista_produtos:
                posicao = lista_produtos.index(nome)
                novo = input("Novo nome: ")
                lista_produtos[posicao] = novo
                print("Produto alterado com sucesso!")
            else:
                print('Produto não encontrado.')
        case 4:
            print('\n== REMOVER PRODUTO ==')
            nome = input('Qual produto deseja remover? ')
            if nome in lista_produtos:
                lista_produtos.remove(nome)
                print("Produto excluído com sucesso!")
            else:
                print("Produto não encontrado.")
        case 5:
            print('\n== ENCONTRAR PRODUTO ==')
            nome = input('Qual produto deseja buscar? ')
            if nome in lista_produtos:
                print("Produto encontrado!")
            else:
                print("Produto não está no estoque.")
        case 0:
            print("Saindo do programa...")
            break
        case _:
            print("Opção inválida! \nTente novamente..")
    input