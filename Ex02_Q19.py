def Horas(hhmm):
    return hhmm // 100

def Minutos(hhmm):
    return hhmm % 100

def TotalMinutos(hhmm):
    return (Horas(hhmm) * 60) + Minutos(hhmm)

def Difereca(hhmm1, hhmm2):
    min1 = TotalMinutos(hhmm1)
    min2 = TotalMinutos(hhmm2)

    return min1 - min2

hhmm = int(input("Digite uma hora no formato HHMM: "))

print("%dh %dmin = %d" % (Horas(hhmm), Minutos(hhmm), TotalMinutos(hhmm)))
