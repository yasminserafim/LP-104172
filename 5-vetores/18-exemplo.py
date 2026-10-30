import os

lista_nome = []
lista_codigo = []
lista_paciente = []

while True:
    os.system("cls")
    print('''
    === HOSPITAL DENDEZEIROS ===
        1 - CADASTRAR PACIENTE
        2 - LISTAR TODOS OS PACIENTES
        3 - ATUALIZAR PACIENTE
        4 - REMOVER PACIENTE
        5 - BUSCA DE PACIENTES
        0 - SAIR
    ''')

    opcao = int(input("Escolha uma opção: "))

    match opcao:
        case 1:
            print("=== CADASTRAR PACIENTE ===")
            nome_sobrenome = str(input("Digite o nome e sobrenome do paciente: ")).strip().upper()
            if nome_sobrenome in lista_nome:
                print("Paciente já cadastrado.")
            else:
                lista_nome.append(nome_sobrenome)
                print("Paciente cadastrado com sucesso.")
            codigo = int(input("Gere um codigo para o paciente: "))
            if codigo in lista_codigo:
                print("Codigo já cadastrado.")
            else:
                lista_codigo.append(codigo)
                print("Codigo cadastrado com sucesso.")
            codigo_nome = [nome_sobrenome, codigo]
            lista_paciente.append(codigo_nome)
            input("\nPressione ENTER para continuar...")
        case 2:
            print("=== LISTAR PACIENTES ===")
            for paciente in lista_paciente:
                print(f"Nome: {paciente[0]}")
                print(f"Código: {paciente[1]}")
            print(f'Total: {len(lista_paciente)}')
            input("\nPressione ENTER para continuar...")
        case 3:
            print('=== ATUALIZAR PACIENTE ===')
            codigo = int(input("Qual paciente deseja atualizar? "))
            if codigo in lista_codigo:
                posicao = lista_codigo.index(codigo)
                novo = input("Novo nome: ")
                lista_nome[posicao] = novo
                print("Paciente alterado com sucesso.")
            else:
                print('Paciente não encontrado.')
            input("\nPressione ENTER para continuar...")
        case 4:
            print('\n=== REMOVER PRODUTO ===')
            nome = input('Qual paciente deseja remover? ')
            codigo = int(input('Qual paciente deseja remover? '))
            if paciente in lista_paciente:
                lista_paciente.remove(nome)
                print("Paciente excluído.")
            else:
                print("Paciente não encontrado.")