import os
os.system("cls")

# ENTRADA
picanha = 1
lasanha = 2
strogonoff = 3
bife_acebolado = 4
pao_com_ovo = 5

# MENU
print('''
=== MENU ===
1 - PICANHA - R$ 25,00
2 - LASANHA - R$ 20,00
3 - STROGONOFF - R$ 18,00
4 - BIFE ACEBOLADO - R$ 15,00
5 - PÃO COM OVO - R$ 5,00
''')

# PROCESSAMENTO
pedido = int(input("Digite o código do seu pedido: "))
match pedido:
    case 1:
        prato = "picanha"
        valor = 25
    case 2:
        prato = "lasanha"
        valor = 20
    case 3:
        prato = "strogonoff"
        valor = 18
    case 4:
        prato = "bife acebolado"
        valor = 15
    case 5:
        prato = "pão com ovo"
        valor = 5
    case _:
        valor = "invalido"

print("Exibindo os resultados:")
print("Seu prato: ", prato)
print("Código do pedido", pedido)
print("Valor do prato: ", valor)