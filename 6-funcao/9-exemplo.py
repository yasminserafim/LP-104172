import os
os.system("cls")

def verificar_positivo_negativo(numero):
    if numero <0:
        resultado = "Negativo"
    else:
        resultado = "Positivo"
    return resultado

print("== SOLICITANDO DADOS ==")
numero = int(input("Digite um número: "))

resultado = verificar_positivo_negativo(numero)

print('\n= EXIBINDO DADOS =')
print(f'O número: {numero} é {resultado}')