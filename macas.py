import os
os.system("cls")

# ENTRADA
quant_macas = int(input("Digite a quantidade de maçãs desejadas: "))

# PROCESSAMENTO
if quant_macas < 12:
    preco = 1.30
else: preco = 1.00

valor_total = quant_macas * preco

# SAÍDA
print("Valor total: ", valor_total)
    


