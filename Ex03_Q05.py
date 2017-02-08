# Crie uma função que recebe um número por parâmetro e
# retorna o valor booleano verdadeiro se o número for par

def EPar(n):
    return n % 2 == 0

def EImpar(n):
    return not EPar(n)

print(EPar(2))
print(EImpar(2))
print(EPar(3))
print(EImpar(3))
