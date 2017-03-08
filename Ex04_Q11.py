# Dado um país A, com 5.000.000 de habitantes e uma taxa de
# natalidade de 3% ao ano, e um país B com 7.000.000 de
# habitantes e uma taxa de natalidade de 2% ano ano.
# Calcular e imprimir o tempo necessário para que a população
# do país A ultrapasse a população do país B.

def CalculaTempo(populacaoA, taxaA, populacaoB, taxaB):
    ano = 0
    while (populacaoA <= populacaoB):
        populacaoA = populacaoA * (1 + (taxaA/100))
        populacaoB = populacaoB * (1 + (taxaB/100))
        ano += 1
    return ano

print("Tempo:", CalculaTempo(5000000, 3, 7000000, 2))

