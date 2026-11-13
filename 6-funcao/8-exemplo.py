import os
os.system("cls")

def verificar_par_impar(numero):
    if numero % 2 == 0:
        resultado = "Par"
    else:
        resultado = "Ímpar"
    return resultado

print("== SOLICITANDO DADOS ==")
numero = int(input("Digite um número: "))

resultado = verificar_par_impar(numero)

print('\n= EXIBINDO DADOS =')
print(f'O número: {numero é {resultado}}')