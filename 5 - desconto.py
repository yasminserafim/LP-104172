import os
os.system("cls")

print("= SOLICITANDO DADOS =")
valor = float(input("Digite o valor: "))

desconto = valor * 0.1
valor_com_desconto = valor - desconto

print("\n= EXIBINDO DADOS =")
print("Valor com desconto: ", valor_com_desconto)