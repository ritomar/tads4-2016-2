def AreaQuadrado(lado):
    return lado * lado

def PerimetroQuadrado(lado):
    return lado * 4

lado = float(input("Digite o lado do quadrado: "))

print("Área: %.2f" % AreaQuadrado(lado))
print("Perímetro: %.2f" % PerimetroQuadrado(lado))
