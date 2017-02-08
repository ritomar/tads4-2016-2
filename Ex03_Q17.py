# A partir de dois números fornecidos pelo usuário,
# escreva uma das seguintes mensagens:
#  - Os dois são pares
#  - Os dois são impares
#  - O primeiro é par e o segundo é ímpar
#  - O primeiro é ímpar e o segundo é par

def EPar(n):
    return n % 2 == 0

def EImpar(n):
    return not EPar(n)

def TesteParImpar(a, b):
    if EPar(a) and EPar(b):
        return "Os dois são pares"
    elif EImpar(a) and EImpar(b):
        return "Os dois são impares"
    elif EPar(a) and EImpar(b):
        return "O primeiro é par e o segundo é ímpar"
    elif EImpar(a) and EPar(b):
        return "O primeiro é ímpar e o segundo é par"

n1 = int(input("Primeiro número: "))
n2 = int(input("Segundo número: "))

print(TesteParImpar(n1, n2))
