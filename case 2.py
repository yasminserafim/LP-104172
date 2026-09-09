import os
os.system("cls")

numero = int(input("Digite um numero: "))

match numero:
    case "1":
        print("Final de Semana")
    case "7":
        print("Final de Semana")
    case "2":
        print("Dia útil")
    case "3":
        print("Dia útil")
    case "4":
        print("Dia útil")
    case "5":
        print("Dia útil")
    case "6":
        print("Dia útil")
    case _:
        print("Dia inválido")