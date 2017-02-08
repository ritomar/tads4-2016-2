# Faça uma função que recebe três números por
# parâmetro e imprime na tela em ordem crescente.

def ImprimeOrdenado(a, b, c):
    if (a < b) and (a < c):
        if (b < c):
            print(a, b, c)
        else:
            print(a, c, b)
    elif (b < a) and (b < c):
        if (a < c):
            print(b, a, c)
        else:
            print(b, c, a)
    else:
        if (a < b):
            print(c, a, b)
        else:
            print(c, b, a)

ImprimeOrdenado(1, 2, 3)
ImprimeOrdenado(2, 3, 1)
ImprimeOrdenado(3, 1, 2)

