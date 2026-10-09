import os
import time

soma_salario = 0
contador_pessoas = 0
mulheres_5K = 0
maior_idade = 0
menor_idade = 999
mulheres_5K = 0

while True:
    os.system("cls")
    print('''
= = = MENU = = = 
1 - Adicionar pessoa
2 - Exibir Resultados
3 - Sair
    ''')
    opcao = int(input("Digite a opção desejada: "))

    match opcao:
        case 1:
            print("= = = CADASTRO = = =")
            idade = int(input("Digite sua idade: "))
            sexo = str(input("Digite o seu sexo (M ou F): "))
            salario = float(input("Digite o salário: R$"))

            soma_salario += salario
            contador_pessoas += 1
            maior_idade = max(idade, maior_idade)
            menor_idade = min(idade, maior_idade)

            if sexo == "F" and salario >= 5000:
                mulheres_5K += 1

                print("Pessoa adicionada com sucessor!")
                input("Presssione uma tecla para continuar...")
        case 2:
            if contador_pessoas == 0:
                print("Nenhuma pessoa cadastrada.")
            else:
                media_salario = soma_salario / contador_pessoas

                print("= = = RESULTADO DA PESQUISA = = =")
                print("Média de salário de grupo: ", media_salario)
                print("Maior idade: ", maior_idade)
                print("Menor idade: ", menor_idade)
                print("Mulheres com salário a partir de R$ 5.000", mulheres_5K)
                input("Pressione uma tecla para continuar...")
        case 3:
                print("Encerrando o programa")
                break
        case _:
            print("Opção Inválida")
            input("Pressione uma tecla para continuar...")