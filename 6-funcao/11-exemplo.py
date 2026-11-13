import os
os.system("cls")

valor_metro = float(input("Digite um valor em metro:"))

def converter_metro_cm(valor_metro):
    resultado = valor_metro * 1000
    return resultado

resultado = converter_metro_cm

print("= EXIBINDO RESULTADO =")
print(f"Resultado: {resultado}")