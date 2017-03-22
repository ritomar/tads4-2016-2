def MesExtenso(mes):
    if mes == 1:
        return 'Janeiro'
    elif mes == 2:
        return 'Fevereiro'
    elif mes == 3:
        return 'Março'
    elif mes == 4:
        return 'Abril'
    elif mes == 5:
        return 'Maio'
    elif mes == 6:
        return 'Junho'
    elif mes == 7:
        return 'Julho'
    elif mes == 8:
        return 'Agosto'
    elif mes == 9:
        return 'Setembro'
    elif mes == 10:
        return 'Outubro'
    elif mes == 11:
        return 'Novembro'
    elif mes == 12:
        return 'Dezembro'
    else:
        return 'Mês inválido'

def LerTemperatura():
    TemperaturaMeses = []
    for i in range(12):
        temperatura = float(input("Temperatura de %s:" % MesExtenso(i + 1)))
        TemperaturaMeses.append(temperatura)
    return TemperaturaMeses

def MediaAnual(Temperaturas):
    soma = 0
    for k in Temperaturas:
        soma += k
    return soma / len(Temperaturas)

def AcimaMedia(Temperaturas):
    media = MediaAnual(Temperaturas)
    Acima_Media = []
    for i in range(len(Temperaturas)):
        if Temperaturas[i] > media:
            Acima_Media.append(MesExtenso(i+1) + ": " + str(k))
    return Acima_Media


Lista_Temperaturas = LerTemperatura()
print('Média anual:', MediaAnual(Lista_Temperaturas))
print(AcimaMedia(Lista_Temperaturas))






    
