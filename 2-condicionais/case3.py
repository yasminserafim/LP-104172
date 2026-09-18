import os
os.system("cls")

# ENTRADA
numero1 = int(input("Digite um numero: "))
numero2 = int(input("Digite outro numero: "))
operacao = str(input("Digite um caractere: "))

# PROCESSAMENTO
match operacao:
    case "*":
        resultado = numero1 * numero2
    case "+":
        resultado = numero1 + numero2
    case "-":
        resultado = numero1 - numero2
    case "/":
        resultado = numero1 / numero2
    case _:
        resultado = "invalido"

# SAÍDA
print("Exibindo resultados:")
print(numero1)
print(numero2)
print(operacao)
print(resultado)

