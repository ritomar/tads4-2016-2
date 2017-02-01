def SaqueTAA(valor):
    notas50 = valor // 50
    valor = valor % 50

    notas10 = valor // 10
    valor = valor % 10

    notas5 = valor // 5
    valor = valor % 5

    notas1 = valor

    return "R$50.00 x %d; R$10.00 x %d; R$5.00 x %d; R$1.00 x %d" % (notas50, notas10, notas5, notas1)

valor = 87
print("Saque no valor de", valor, "notas:\n", SaqueTAA(87))
