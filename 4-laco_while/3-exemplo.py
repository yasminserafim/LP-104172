import os
os.system("cls")

print('''
= = = MENU = = =
BOLO R$ 25,00
SORVETE R$ 10,00
BRIGADEIRO R$ 3,00
PUDIM R$ 15,00
MOUSSE 10 R$ 10,00
''')

bolo_preco = 25
sorvete_preco = 10
brigadeiro_preco = 3
pudim_preco = 15
mousse_preco = 10

pedido = str(input("Digite seu pedido: "))

while True:
    if pedido == "bolo":
        print("Seu pedido: ", pedido)
        print("Preço: ", bolo_preco)
        break
    elif pedido == "sorvete":
        print("Seu pedido: ", pedido)
        print("Preço: ", sorvete_preco)
        break
    elif pedido == "brigadeiro":
        print("Seu pedido: ", pedido)
        print("Preço: ", brigadeiro_preco)
        break
    elif pedido == "pudim":
        print("Seu pedido: ", pedido)
        print("Preço: ", pudim_preco)
        break
    elif pedido == "mousse":
        print("Seu pedido: ", pedido)
        print("Preço: ", mousse_preco)
        break
    else:
        print("Inválido")