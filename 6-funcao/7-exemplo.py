import os 
os.system("cls")

def calcular_notas(nota1, nota2):
    resultado = (nota1 + nota2) / 2
    return resultado

print("= SOLICITANDO NOTAS =")
nota1 = float(input("Digite a primeira nota: "))
nota2 = float(input("Digite a segunda nota: "))

def verificar_resultado(media):
    if media >=7:
        resultado = "Aprovado"
    else:
        resultado = "Reprovado"

#usando a função com parametro
#e inserindo o retorno na variavel soma.
media = calcular_notas(nota1, nota2)
situacao = verificar_resultado(media)

print("= EXIBINDO NOTAS =")
print(f"Média: {media}")
