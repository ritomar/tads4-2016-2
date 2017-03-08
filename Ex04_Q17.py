def SomaH(N):
    H = 0
    for i in range(1, N + 1):
        H += 1/i
    return H

k = int(input("Digite o valor de N: "))
print("Soma H(%d) = " % k, SomaH(k))
