import os
os.system("cls")

# CRIANDO UMA FUNÇÃO
def cabecalho():
    print('\n')
    print('='*15)
    print(' SENAI BAHIA')
    print('='*15)

cabecalho() #USANDO A FUNÇÃO
nome = input('Digite seu nome: ')

cabecalho() #USANDO A FUNÇÃO
idade = input('Digite sua idade: ')

cabecalho() #USANDO A FUNÇÃO
print(f'Nome: {nome}')
print(f'Idade: {idade}')
