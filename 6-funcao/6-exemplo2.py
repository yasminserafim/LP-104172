import os
os.system("cls")

def logo_senai():
    print("==========")
    print("    SENAI")
    print("==========")

def mostrar_dados(nome, idade):
    print(f'{nome} tem {idade} anos.')

logo_senai()
print("\n== SOLICITANDO DADOS ==")
nome = input("Digite seu nome: ")
idade = input("Digite sua idade: ")

logo_senai()
print("== EXIBINDO DADOS ==")
# função sem retorno e com parametros
mostrar_dados(nome, idade)