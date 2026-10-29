import os
lista_produtos = []


while True:
    # limpar terminal
    os.system("cls")

    # MENU DO PROGRAMA
    print('''
=== MERCADINHO DENDEZEIROS ===
1 - CADASTRAR PRODUTOS 
2 - LISTAR PRODUTOS
0 - SAIR
    ''')

    opcao = int(input("Escolha uma opção: "))

    match opcao:
        case 1:
            print("\n== CADASTRAR UM PRODUTO ==")
            # STRIP() RETIRAR OS ESPAÇOS VAZIOS NO FINAL
            # UPPER () TODAS AS LETRAS MAIUSCULAS
            nome = str(input("Nome do novo produto: ")).strip().upper()

            if nome == '':
                print('Escreva o nome do produto.')
            elif nome in lista_produtos:
                print(f'{nome} já cadastrado.')
            else:
                # APPEND (NOME) ADICIONA O NOME DO PRODUTO NA LISTA.
                lista_produtos.append(nome)
                print("Produto cadastrado com sucesso!")

        case 2:
            print("\n== PRODUTOS NO ESTOQUE ==")
            for i, produto in enumerate(lista_produtos):
                print(f'{i+1}. {produto}')
            # LEN(LISTA_PRODUTOS) MOSTRA A QUANTIDADE DE PRODUTOS NA LISTA
            print(f'Total de produtos: {len(lista_produtos)}')
            input('Pressione uma tecla para continuar...')

        case 0:
            print("Fim do programa.")
            break
        
        case _:
            print("Opção inválida!")
            input("\nPressione uma tecla para continuar")