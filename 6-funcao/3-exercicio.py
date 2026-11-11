import os

def mostrar_dados(nome, email, telefone):
    print(f'Nome: {nome}')
    print(f'Email: {email}')
    print(f'Telefone: {telefone}')

def logo_senai():
    os.system("cls")
    print('\n')
    print('='*12)
    print(' SENAI BAHIA')
    print('='*12)

logo_senai()
nome = input('Digite seu nome: ')
logo_senai()
email = input('Digite seu email: ')
logo_senai()
telefone = input('Digite seu telefone: ')

print('\n= Exibindo dados =')
mostrar_dados(nome, email, telefone)