import os
os.system("cls")

import os 
os.system("cls")

def calcular_soma(numero1, numero2):
    resultado_soma = numero1 + numero2
    return resultado_soma

def calcular_sub(numero1, numero2):
    resultado_sub = numero1 - numero2
    return resultado_sub

def calcular_mult(numero1, numero2):
    resultado_mult = numero1 * numero2
    return resultado_mult

def calcular_div(numero1, numero2):
    if numero2 == 0:
        return 'Atenção! Divisão por zero.'
    resultado_div = numero1 / numero2
    return resultado_div

print("= SOLICITANDO NOTAS =")
numero1 = int(input("Digite o primeiro número: "))
numero2 = int(input("Digite o segundo número: "))


#usando a função com parametro
#e inserindo o retorno na variavel soma.
soma = calcular_soma(numero1, numero2)
sub = calcular_sub(numero1, numero2)
mult = calcular_mult(numero1, numero2)
div = calcular_div(numero1, numero2)

print("= EXIBINDO NOTAS =")
print(f"Soma: {soma}")
print(f"Subtração: {sub}")
print(f"Multiplicação: {mult}")
print(f"Divisão: {div}")